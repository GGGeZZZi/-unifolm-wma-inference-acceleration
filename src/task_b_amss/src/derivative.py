########################################################################################
##
## This module provides finite-difference routines to compute numerical derivatives.
##
########################################################################################

import numpy

########################################################################################

## first_order_derivative(f, x, dx, method)
## Compute the first derivative of a scalar function f(x) using centered finite-difference stencils.
##
## Inputs:
##  - f: callable f(x)
##  - x: evaluation point (float)
##  - dx: grid spacing (float)
##  - method: stencil identifier string; one of
##      "3-points 2-orders", "5-points 4-orders", "7-points 6-orders"

def first_order_derivative( f, x, dx, method ):
    
    h = dx

    # Centered 2nd-order difference:
    # df/dx = ( f(x+h) - f(x-h) ) / (2 h)
    if method == "3-points 2-orders":
        df_dx = ( f(x+h) - f(x-h) ) / ( 2.0*h )

    # Centered 4th-order (five-point) stencil:
    # df/dx = ( f(x-2h) - 8 f(x-h) + 8 f(x+h) - f(x+2h) ) / (12 h)
    elif method == "5-points 4-orders":
        df_dx = ( f(x-2.0*h) - 8.0*f(x-h) + 8.0*f(x+h) - f(x+2.0*h) ) / ( 12.0*h )

    # Centered 6th-order (seven-point) stencil:
    # df/dx = ( -f(x-3h) + 9 f(x-2h) - 45 f(x-h) + 45 f(x+h) - 9 f(x+2h) + f(x+3h) ) / (60 h)
    elif method == "7-points 6-orders":
        df_dx = ( - f(x-3.0*h) + 9.0*f(x-2.0*h) - 45.0*f(x-h) + 45.0*f(x+h) - 9.0*f(x+2.0*h) + f(x+3.0*h) ) / ( 60.0*h )

    return df_dx

########################################################################################

## first_order_derivative_multivalue(f, x, dx, method)
## Compute the first derivative of a multivalued function f(x) that returns
## multiple components (e.g., a tuple or list) at the point x using finite differences.
##
## Inputs:
##  - f: callable that returns an iterable of values at a given x
##  - x: evaluation point (float)
##  - dx: grid spacing (float)
##  - method: stencil identifier string; one of
##      "3-points 2-orders", "5-points 4-orders", "7-points 6-orders"

def first_order_derivative_multivalue( f, x, dx, method ):
    
    # Determine number of components returned by f(x)
    num = len( f(x) )
    
    df_dx = numpy.zeros( num )
    
    # grid spacing
    h = dx

    # Centered 2nd-order difference:
    # df/dx = ( f(x+h) - f(x-h) ) / (2 h)
    if method == "3-points 2-orders":
        f_minus = f(x-h)
        f_plus = f(x+h)
        for i in range(num):
            df_dx[i] = ( f_plus[i] - f_minus[i] ) / ( 2.0*h )

    # Centered 4th-order (five-point) stencil:
    # df/dx = ( f(x-2h) - 8 f(x-h) + 8 f(x+h) - f(x+2h) ) / (12 h)
    elif method == "5-points 4-orders":
        f_minus2 = f(x-2.0*h)
        f_minus1 = f(x-h)
        f_plus1 = f(x+h)
        f_plus2 = f(x+2.0*h)
        for i in range(num):
            df_dx[i] = ( f_minus2[i] - 8.0*f_minus1[i] + 8.0*f_plus1[i] - f_plus2[i] ) / ( 12.0*h )

    # Centered 6th-order (seven-point) stencil:
    # df/dx = ( -f(x-3h) + 9 f(x-2h) - 45 f(x-h) + 45 f(x+h) - 9 f(x+2h) + f(x+3h) ) / (60 h)
    elif method == "7-points 6-orders":
        f_minus3 = f(x-3.0*h)
        f_minus2 = f(x-2.0*h)
        f_minus1 = f(x-h)
        f_plus1 = f(x+h)
        f_plus2 = f(x+2.0*h)
        f_plus3 = f(x+3.0*h)
        for i in range(num):
            df_dx[i] = ( -f_minus3[i] + 9.0*f_minus2[i] - 45.0*f_minus1[i] + 45.0*f_plus1[i] - 9.0*f_plus2[i] + f_plus3[i] ) / ( 60.0*h )

    return df_dx

########################################################################################
