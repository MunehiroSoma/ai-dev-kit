"""Run the same behavioral checks against the input and edited retry examples."""

import importlib.util
import inspect
from pathlib import Path
import unittest
from unittest.mock import Mock, patch


class RetryContract(unittest.TestCase):
    implementation = None

    def setUp(self):
        self.module = self.implementation
        self.sleep_patch = patch.object(self.module.time, "sleep")
        self.warning_patch = patch.object(self.module.logger, "warning")
        self.sleep = self.sleep_patch.start()
        self.warning = self.warning_patch.start()
        self.addCleanup(self.sleep_patch.stop)
        self.addCleanup(self.warning_patch.stop)

    def test_signature(self):
        self.assertEqual(str(inspect.signature(self.module.run_with_retry)),
                         "(operation, attempts=3, delay=1)")

    def test_success_identity(self):
        value = object()
        operation = Mock(return_value=value)
        self.assertIs(self.module.run_with_retry(operation), value)
        operation.assert_called_once_with()
        self.sleep.assert_not_called()
        self.warning.assert_not_called()

    def test_none_result(self):
        operation = Mock(return_value=None)
        self.assertIsNone(self.module.run_with_retry(operation))
        operation.assert_called_once_with()

    def test_invalid_attempts_before_operation(self):
        for attempts in (0, -1, True, False, 1.5, "3"):
            with self.subTest(attempts=attempts):
                operation = Mock()
                with self.assertRaises(ValueError):
                    self.module.run_with_retry(operation, attempts=attempts)
                operation.assert_not_called()

    def test_negative_delay_before_operation(self):
        operation = Mock()
        with self.assertRaises(ValueError):
            self.module.run_with_retry(operation, delay=-1)
        operation.assert_not_called()

    def test_retry_then_success(self):
        value = object()
        operation = Mock(side_effect=[self.module.RetryableError(),
                                     self.module.RetryableError(), value])
        self.assertIs(self.module.run_with_retry(operation, delay=0.25), value)
        self.assertEqual(operation.call_count, 3)
        self.assertEqual(self.sleep.call_count, 2)
        self.assertTrue(all(call.args == (0.25,) for call in self.sleep.call_args_list))
        self.assertEqual(self.warning.call_count, 2)

    def test_exhaustion_preserves_exception(self):
        error = self.module.RetryableError("lock")
        operation = Mock(side_effect=error)
        with self.assertRaises(self.module.RetryableError) as observed:
            self.module.run_with_retry(operation)
        self.assertIs(observed.exception, error)
        self.assertEqual(operation.call_count, 3)
        self.assertEqual(self.sleep.call_count, 2)
        self.assertEqual(self.warning.call_count, 2)

    def test_nonretry_error(self):
        for error in (RuntimeError("fatal"), KeyboardInterrupt()):
            with self.subTest(error=type(error).__name__):
                operation = Mock(side_effect=error)
                with self.assertRaises(type(error)) as observed:
                    self.module.run_with_retry(operation)
                self.assertIs(observed.exception, error)
                operation.assert_called_once_with()
        self.sleep.assert_not_called()
        self.warning.assert_not_called()

    def test_single_attempt(self):
        operation = Mock(side_effect=self.module.RetryableError())
        with self.assertRaises(self.module.RetryableError):
            self.module.run_with_retry(operation, attempts=1)
        operation.assert_called_once_with()
        self.sleep.assert_not_called()
        self.warning.assert_not_called()

    def test_zero_delay(self):
        operation = Mock(side_effect=[self.module.RetryableError(), "ok"])
        self.assertEqual(self.module.run_with_retry(operation, delay=0), "ok")
        self.sleep.assert_called_once_with(0)

    def test_fatal_after_retry(self):
        error = RuntimeError("fatal")
        operation = Mock(side_effect=[self.module.RetryableError(), error])
        with self.assertRaises(RuntimeError) as observed:
            self.module.run_with_retry(operation)
        self.assertIs(observed.exception, error)
        self.assertEqual(operation.call_count, 2)
        self.sleep.assert_called_once_with(1)
        self.warning.assert_called_once()

    def test_wait_failure(self):
        error = RuntimeError("sleep failed")
        self.sleep.side_effect = error
        operation = Mock(side_effect=self.module.RetryableError())
        with self.assertRaises(RuntimeError) as observed:
            self.module.run_with_retry(operation)
        self.assertIs(observed.exception, error)
        operation.assert_called_once_with()


def main():
    root = Path(__file__).resolve().parent
    success = True
    for name in ("retry-policy-input.py", "outputs/retry_policy.py"):
        spec = importlib.util.spec_from_file_location("retry_example", root / name)
        implementation = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(implementation)
        RetryContract.implementation = implementation
        print(f"Checking {name}", flush=True)
        result = unittest.TextTestRunner(verbosity=2).run(
            unittest.defaultTestLoader.loadTestsFromTestCase(RetryContract))
        success = result.wasSuccessful() and success
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
