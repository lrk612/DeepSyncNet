<<<<<<< HEAD
from scipy.signal import savgol_filter

from .finite_difference import FiniteDifference


class SmoothedFiniteDifference(FiniteDifference):
    """Smoothed finite difference derivatives.

    Perform differentiation by smoothing input data then applying a finite
    difference method.

    Parameters
    ----------
    smoother: function, optional (default :code:`savgol_filter`)
        Function to perform smoothing. Must be compatible with the
        following call signature: :code:`x_smoothed = smoother(x, **smoother_kws)`

    smoother_kws: dict, optional (default :code:`{}`)
        Arguments passed to smoother when it is invoked.

    save_smooth: bool
        Whether to save the smoothed coordinate values or not.

    **kwargs: kwargs
        Additional parameters passed to the :meth:`pysindy.FiniteDifference.__init__`
        function.

    Examples
    --------
    >>> import numpy as np
    >>> from pysindy.differentiation import SmoothedFiniteDifference
    >>> t = np.linspace(0,1,10)
    >>> X = np.vstack((np.sin(t),np.cos(t))).T
    >>> sfd = SmoothedFiniteDifference(smoother_kws={'window_length': 5})
    >>> sfd._differentiate(X, t)
    array([[ 1.00013114e+00,  7.38006789e-04],
           [ 9.91779070e-01, -1.10702304e-01],
           [ 9.73376491e-01, -2.20038119e-01],
           [ 9.43001496e-01, -3.26517615e-01],
           [ 9.00981354e-01, -4.29066632e-01],
           [ 8.47849424e-01, -5.26323977e-01],
           [ 7.84260982e-01, -6.17090177e-01],
           [ 7.11073255e-01, -7.00180971e-01],
           [ 6.29013295e-01, -7.74740601e-01],
           [ 5.39752150e-01, -8.41980082e-01]])
    """

    def __init__(
        self, smoother=savgol_filter, smoother_kws={}, save_smooth=True, **kwargs
    ):
        super(SmoothedFiniteDifference, self).__init__(**kwargs)
        self.smoother = smoother
        self.smoother_kws = smoother_kws
        self.save_smooth = save_smooth

        if smoother is savgol_filter:
            if "window_length" not in smoother_kws:
                self.smoother_kws["window_length"] = 11
            if "polyorder" not in smoother_kws:
                self.smoother_kws["polyorder"] = 3
            self.smoother_kws["axis"] = 0

    def _differentiate(self, x, t):
        """Apply finite difference method after smoothing."""
        x_smooth = self.smoother(x, **self.smoother_kws)
        x_dot = super(SmoothedFiniteDifference, self)._differentiate(x_smooth, t)
        if self.save_smooth:
            self.smoothed_x_ = x_smooth
        else:
            self.smoothed_x_ = x
        return x_dot
=======
from scipy.signal import savgol_filter

from .finite_difference import FiniteDifference


class SmoothedFiniteDifference(FiniteDifference):
    """Smoothed finite difference derivatives.

    Perform differentiation by smoothing input data then applying a finite
    difference method.

    Parameters
    ----------
    smoother: function, optional (default :code:`savgol_filter`)
        Function to perform smoothing. Must be compatible with the
        following call signature: :code:`x_smoothed = smoother(x, **smoother_kws)`

    smoother_kws: dict, optional (default :code:`{}`)
        Arguments passed to smoother when it is invoked.

    save_smooth: bool
        Whether to save the smoothed coordinate values or not.

    **kwargs: kwargs
        Additional parameters passed to the :meth:`pysindy.FiniteDifference.__init__`
        function.

    Examples
    --------
    >>> import numpy as np
    >>> from pysindy.differentiation import SmoothedFiniteDifference
    >>> t = np.linspace(0,1,10)
    >>> X = np.vstack((np.sin(t),np.cos(t))).T
    >>> sfd = SmoothedFiniteDifference(smoother_kws={'window_length': 5})
    >>> sfd._differentiate(X, t)
    array([[ 1.00013114e+00,  7.38006789e-04],
           [ 9.91779070e-01, -1.10702304e-01],
           [ 9.73376491e-01, -2.20038119e-01],
           [ 9.43001496e-01, -3.26517615e-01],
           [ 9.00981354e-01, -4.29066632e-01],
           [ 8.47849424e-01, -5.26323977e-01],
           [ 7.84260982e-01, -6.17090177e-01],
           [ 7.11073255e-01, -7.00180971e-01],
           [ 6.29013295e-01, -7.74740601e-01],
           [ 5.39752150e-01, -8.41980082e-01]])
    """

    def __init__(
        self, smoother=savgol_filter, smoother_kws={}, save_smooth=True, **kwargs
    ):
        super(SmoothedFiniteDifference, self).__init__(**kwargs)
        self.smoother = smoother
        self.smoother_kws = smoother_kws
        self.save_smooth = save_smooth

        if smoother is savgol_filter:
            if "window_length" not in smoother_kws:
                self.smoother_kws["window_length"] = 11
            if "polyorder" not in smoother_kws:
                self.smoother_kws["polyorder"] = 3
            self.smoother_kws["axis"] = 0

    def _differentiate(self, x, t):
        """Apply finite difference method after smoothing."""
        x_smooth = self.smoother(x, **self.smoother_kws)
        x_dot = super(SmoothedFiniteDifference, self)._differentiate(x_smooth, t)
        if self.save_smooth:
            self.smoothed_x_ = x_smooth
        else:
            self.smoothed_x_ = x
        return x_dot
>>>>>>> dc075487f2a58d03645bfca002881f561f1e93d0
