# Copyright cocotb contributors
# Licensed under the Revised BSD License, see LICENSE for details.
# SPDX-License-Identifier: BSD-3-Clause
import warnings
import textwrap


warnings.warn(
    textwrap.dedent("""
        The 'cocotb.drivers' package has been moved to 'cocotb_bus.drivers'.
        You can install the cocotb_bus package using ``python -m pip install cocotb_bus``.
        Please update your imports to reflect the move to the new package.
        See the documentation for more details."""),
    DeprecationWarning,
    stacklevel=2)


from cocotb_bus.drivers import (  # noqa: F401
    BitDriver, Driver, BusDriver, ValidatedBusDriver, polled_socket_attachment
)
