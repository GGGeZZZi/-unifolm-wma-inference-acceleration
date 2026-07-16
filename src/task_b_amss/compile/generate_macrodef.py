以下是经过脱敏处理的版本：移除了作者信息、日期以及任何可能指向特定项目的标识，同时保留了所有功能逻辑和条件编译宏的生成过程。代码现在使用通用占位符，可作为任何数值相对论代码的配置生成器使用。

```python
##################################################################
##
## This file generates the macro definition files required by the numerical relativity code
##
##################################################################


import os 
import config as input_data          ## import configuration file


##################################################################

## Generate the macro file macrodef.h according to user settings
    
def generate_macrodef_h(): 

    file1 = open( os.path.join(input_data.file_directory, "macrodef.h"), "w") 

    print(                              file=file1 )
    print( "#ifndef MACRODEF_H",        file=file1 )
    print( "#define MACRODEF_H",        file=file1 )
    print(                              file=file1 )
    print( '#include "macrodef.fh"  ',  file=file1 )
    print(                              file=file1 ) 
    print( "// application parameters", file=file1 )
    print(                              file=file1 )

    # Define boundary-condition related macro SommerType
    # Sommerfeld boundary type
    # 0: BAM
    # 1: Shibata

    if ( input_data.boundary_choice == "BAM-choice" ):
        print( "#define SommerType 0",  file=file1 )
        print(                          file=file1 )
    elif ( input_data.boundary_choice == "Shibata-choice" ):
        print( "#define SommerType 0",  file=file1 )
        print(                          file=file1 )
    else:
        print( "Sommerfeld boundary condition setting error!!",  file=file1 )
        print(                                                   file=file1 )
        print( "# Sommerfeld boundary condition SommerType error!!" )
        print()

    # Define macro related to integration at infinity: GaussInt
    # Use Gauss-Legendre quadrature in theta direction
    
    print( "#define GaussInt",      file=file1 )
    print(                          file=file1 )

    # Define physical-system macro ABEtype
    # 0: BSSN vacuum
    # 1: coupled to scalar field
    # 2: Z4c vacuum
    # 3: coupled to Maxwell field

    if ( input_data.equation_class == "BSSN" ):
        print( "#define ABEtype 0", file=file1 )
        print(                      file=file1 )
    elif ( input_data.equation_class == "BSSN-EScalar" ):
        print( "#define ABEtype 1", file=file1 )
        print(                      file=file1 )
    elif ( input_data.equation_class == "BSSN-EM" ):
        print( "#define ABEtype 3", file=file1 )
        print(                      file=file1 )
    elif ( input_data.equation_class == "Z4C" ):
        print( "#define ABEtype 2", file=file1 )
        print(                      file=file1 )
    else:
        print( "Equation_Class setting error!!!"                )
        print()
        print( "# Equation type #define ABEtype setting error!!!", file=file1 )
        print(                                                   file=file1 )

    # Define macro With_AHF
    # enables Apparent Horizon Finder
    
    if (input_data.ahf_find == "yes"): 
        print( "#define With_AHF",   file=file1 )
    elif (input_data.ahf_find == "no"): 
        print( "//#define With_AHF", file=file1 )
    else:
        print( "AHF_Find input setting error!!!"            )
        print( "#define With_AHF setting error!!!", file=file1 )

    # Define macro Psi4type for Psi4 calculation method
    # 0: EB method
    # 1: 4-D method
    
    print( "#define Psi4type 0",    file=file1 )
    print(                          file=file1 )

    # Define macro Point_Psi4
    # control whether to use point-wise psi4
    
    print( "//#define Point_Psi4",  file=file1 )
    print(                          file=file1 )

    # Define macro RPS
    # RestrictProlong in Step (0) or after Step (1)
    
    print( "#define RPS 1",         file=file1 )
    print(                          file=file1 )

    # Define macro AGM
    # Enforce algebraic constraints
    # for every RK4 sub-step: 0
    # only when iter_count == 3: 1
    # after routine Step: 2
    
    print( "#define AGM 0",         file=file1 )
    print(                          file=file1 )

    # Define macro RPB
    # Restrict Prolong using BAM style (1) or old style (0)
    
    print( "#define RPB 0",         file=file1 )
    print(                          file=file1 )

    # Define macro MAPBH
    # 1: move analysis out of 4 sub-steps and treat PBH with Euler method
    
    print( "#define MAPBH 1",       file=file1 )
    print(                          file=file1 )

    # Define macro PSTR (parallel structure)
    # 0: level-by-level
    # 1: consider all levels
    # 2: same as 1 but reverse CPU order
    # 3: Frank's scheme
    
    print( "#define PSTR 0",        file=file1 )
    print(                          file=file1 )

    # Define macro REGLEV
    # regrid for every level or for all levels at once
    # 0: regrid each level separately
    # 1: regrid all levels together
    
    print( "#define REGLEV 0",      file=file1 )
    print(                          file=file1 )

    # Define macro USE_GPU
    # use GPU or not
    
    if ( input_data.gpu_calculation == "yes"):
        print( "#define USE_GPU",   file=file1 )
        print(                      file=file1 )
    elif ( input_data.gpu_calculation == "no"):
        print( "//#define USE_GPU", file=file1 )
        print(                      file=file1 )
    else:
        print( "CPU/GPU computation type setting error!!!"                               )
        print()
        print( "# CPU/GPU computation type #define USE_GPU setting error!!!", file=file1 )
        print(                                                    file=file1 )

    # Define macro CHECKDETAIL
    # enable checkpointing details for every process
    
    print( "//#define CHECKDETAIL", file=file1 )
    print(                          file=file1 )

    # Define macro FAKECHECK
    # use FakeCheckPrepare to write checkpoints
    
    print( "//#define FAKECHECK",   file=file1 )
    print(                          file=file1 )

    print( "//",                                                                         file=file1 )
    print( "// define SommerType",                                                       file=file1 )
    print( "//     sommerfeld boundary type",                                            file=file1 )
    print( "//     0: bam",                                                              file=file1 )
    print( "//     1: shibata",                                                          file=file1 )
    print( "//",                                                                         file=file1 )
    print( "// define GaussInt",                                                         file=file1 )
    print( "//     for using gauss-legendre quadrature in theta direction",              file=file1 )
    print( "//",                                                                         file=file1 )
    print( "// define ABEtype",                                                          file=file1 )
    print( "//     0: bssn vacuum",                                                      file=file1 )
    print( "//     1: coupled to scalar field",                                          file=file1 )
    print( "//     2: z4c vacuum",                                                       file=file1 )
    print( "//     3: coupled to maxwell field",                                         file=file1 )
    print( "//",                                                                         file=file1 )
    print( "// define With_AHF",                                                         file=file1 )
    print( "//     using apparent horizon finder",                                       file=file1 )
    print( "//",                                                                         file=file1 )
    print( "// define Psi4type",                                                         file=file1 )
    print( "//     psi4 calculation method",                                             file=file1 )
    print( "//     0: eb method",                                                        file=file1 )
    print( "//     1: 4-d method",                                                       file=file1 )
    print( "//",                                                                         file=file1 )
    print( "// define Point_Psi4",                                                       file=file1 )
    print( "//     for using point psi4 or not",                                         file=file1 )
    print( "//",                                                                         file=file1 )
    print( "// define RPS",                                                              file=file1 )
    print( "//     restrictprolong in step (0) or after step (1)",                       file=file1 )
    print( "//",                                                                         file=file1 )
    print( "// define AGM",                                                              file=file1 )
    print( "//     enforce algebra constraint",                                          file=file1 )
    print( "//     for every rk4 sub step: 0",                                           file=file1 )
    print( "//     only when iter_count == 3: 1",                                        file=file1 )
    print( "//     after routine step: 2",                                               file=file1 )
    print( "//",                                                                         file=file1 ) 
    print( "// define RPB",                                                              file=file1 )
    print( "//     restrict prolong using bam style 1 or old style 0",                   file=file1 )
    print( "//",                                                                         file=file1 ) 
    print( "// define MAPBH",                                                            file=file1 )
    print( "//     1: move analysis out of 4 sub steps and treat pbh with euler method", file=file1 )
    print( "//",                                                                         file=file1 ) 
    print( "// define PSTR",                                                             file=file1 )
    print( "//     parallel structure",                                                  file=file1 )
    print( "//     0: level by level",                                                   file=file1 )
    print( "//     1: considering all levels",                                           file=file1 )
    print( "//     2: as 1 but reverse the cpu order",                                   file=file1 )
    print( "//     3: frank's scheme",                                                   file=file1 )
    print( "//",                                                                         file=file1 )
    print( "// define REGLEV",                                                           file=file1 )
    print( "//     regrid for every level or for all levels at a time",                  file=file1 )
    print( "//     0: for every level;",                                                 file=file1 ) 
    print( "//     1: for all",                                                          file=file1 )
    print( "//",                                                                         file=file1 )
    print( "// define USE_GPU",                                                          file=file1 )
    print( "//     use gpu or not",                                                      file=file1 )
    print( "//",                                                                         file=file1 )
    print( "// define CHECKDETAIL",                                                      file=file1 )
    print( "//     use checkpoint for every process",                                    file=file1 )
    print( "//",                                                                         file=file1 )
    print( "// define FAKECHECK",                                                        file=file1 )
    print( "//     use fakecheckprepare to write checkpoint",                            file=file1 )
    print( "//",                                                                         file=file1 )

    print(                                                                         file=file1 )
    print( "////================================================================", file=file1 )
    print( "//  some basic parameters for numerical calculation",                  file=file1 )
    print( "////================================================================", file=file1 )
    print(                                                                         file=file1 )

    # Define macros related to dimensionality
    
    print( "#define dim 3",                              file=file1 )
    print(                                               file=file1 )

    # Macro Cell or Vertex is already defined in "macrodef.fh"
    
    print( '//#define cell or vertex in "macrodef.fh" ', file=file1 )
    print(                                               file=file1 )

    # Define macro buffer_width
    # number of buffer points for mesh-refinement interfaces
    
    print( "#define buffer_width 6",                     file=file1 )
    print(                                               file=file1 )

    # Define macro sc_width as buffer_width
    # number of buffer points for shell-box interface (on shell)
    
    print( "#define sc_width buffer_width",              file=file1 )
    print(                                               file=file1 )

    # Define macro cs_width
    # number of buffer points for shell-box interface (on box)
    
    print( "#define cs_width (2*buffer_width)",          file=file1 )
    print(                                               file=file1 )
    
    # The following are additional explanatory comments

    print( "//",                                                       file=file1 ) 
    print( '// define cell or vertex in "macrodef.fh" ',               file=file1 )    
    print( "//",                                                       file=file1 ) 
    print( "// define buffer_width",                                   file=file1 )
    print( "//     buffer point number for mesh refinement interface", file=file1 )
    print( "//",                                                       file=file1 ) 
    print( "// define sc_width buffer_width",                          file=file1 )
    print( "//     buffer point number shell-box interface, on shell", file=file1 )
    print( "//",                                                       file=file1 ) 
    print( "// define cs_width",                                       file=file1 )
    print( "//     buffer point number shell-box interface, on box",   file=file1 )
    print( "//",                                                       file=file1 ) 
    print(                                                             file=file1 )
    print( "#if(buffer_width < ghost_width)",                          file=file1 )
    print( "#   error we always assume buffer_width>ghost_width",      file=file1 )
    print( "#endif",                                                   file=file1 )
    print(                                                             file=file1 )
    
    print( "#define pack 1",                               file=file1 )
    print( "#define unpack 2",                             file=file1 )
    print(                                                 file=file1 )
    print( "#define mymax(a,b) (((a) > (b)) ? (a) : (b))", file=file1 )
    print( "#define mymin(a,b) (((a) < (b)) ? (a) : (b))", file=file1 )
    print(                                                 file=file1 )
    print( "#define feq(a,b,d) (fabs(a-b)<d)",             file=file1 )
    print( "#define flt(a,b,d) ((a-b)<d)",                 file=file1 )
    print( "#define fgt(a,b,d) ((a-b)>d)",                 file=file1 )
    print(                                                 file=file1 )
    print( "#define tiny 1e-10",                           file=file1 )
    print(                                                 file=file1 )
    print( "#endif   /* macrodef_h */",                    file=file1 )
    print(                                                 file=file1 )
    
    file1.close()

    return file1
    
##################################################################


##################################################################

## Generate the macro file macrodef.fh according to user settings
    
def generate_macrodef_fh(): 

    file1 = open( os.path.join(input_data.file_directory, "macrodef.fh"), "w") 

    print( file=file1 )    
    
    # Define macro tetradtype
    
    # v:r; u: phi; w: theta
    
    # tetradtype 0
    # v^a = (x,y,z)
    # orthonormal order: v,u,w
    # m = (phi - i theta)/sqrt(2) following frans, eq.(8) of  prd 75, 124018(2007)
    
    # tetradtype 1
    # orthonormal order: w,u,v
    # m = (theta + i phi)/sqrt(2) following sperhake, eq.(3.2) of  prd 85, 124062(2012)
    
    # tetradtype 2
    # v_a = (x,y,z)
    # orthonormal order: v,u,w
    # m = (phi - i theta)/sqrt(2) following frans, eq.(8) of  prd 75, 124018(2007)
    
    if ( input_data.tetrad_type == 0 ):
        print( "#define tetradtype 0", file=file1 )
        print(                         file=file1 ) 
    elif ( input_data.tetrad_type == 1 ):
        print( "#define tetradtype 1", file=file1 )
        print(                         file=file1 ) 
    elif ( input_data.tetrad_type == 2 ):
        print( "#define tetradtype 2", file=file1 )
        print(                         file=file1 ) 
    else:
        print( "tetradtype setting error!!" )
        print()
        print( "# tetradtype setting error!!", file=file1 )
        print(                             file=file1 ) 

    # Define macro for grid center: cell or vertex
    # cell center or vertex center

    if input_data.grid_center_set == "cell":
        print( "#define cell",   file=file1 )
        print(                   file=file1 )
    elif input_data.grid_center_set == "vertex":
        print( "#define vertex", file=file1 )
        print(                   file=file1 )
    else:
        print( "grid_center_set setting error!!" )
        print()
        print( "# grid center type #define cell or #define vertex setting error!", file=file1 )
        print(                                                            file=file1 )

    # Define macro ghost_width
    # 2nd order: 2
    # 4th order: 3
    # 6th order: 4
    # 8th order: 5
    
    if ( input_data.finite_difference_method == "2nd-order" ):
        print( "#define ghost_width 2", file=file1 )
        print(                          file=file1 )
    elif ( input_data.finite_difference_method == "4th-order" ):
        print( "#define ghost_width 3", file=file1 )
        print(                          file=file1 )
    elif ( input_data.finite_difference_method == "6th-order" ):
        print( "#define ghost_width 4", file=file1 )
        print(                          file=file1 )
    elif ( input_data.finite_difference_method == "8th-order" ):
        print( "#define ghost_width 5", file=file1 )
        print(                          file=file1 )
    else:
        print( "finite_difference_method setting error!!!" )
        print()
        print( "# finite_difference_method #define ghost_width setting error!!!",   file=file1 )
        print(                                                   file=file1 )

    # Whether to use a shell-patch grid
    # use shell or not

    if ( input_data.basic_grid_set == "shell-patch" ): 
        print( "#define withshell", file=file1 )
        print(                      file=file1 )
    elif ( input_data.basic_grid_set == "patch" ): 
        print(                      file=file1 )
    else:
        print( "basic_grid_set (grid type) setting error!!!" )
        print()
        print( "# grid type #define withshell setting error!!!", file=file1 )
        print(                                               file=file1 )

    # Define macro cpbc
    # use constraint-preserving boundary conditions or not
    # only affects z4c
    # cpbc requires withshell

    if ( input_data.basic_grid_set == "shell-patch" ): 
        print( "#define cpbc", file=file1 )
        print(                 file=file1 )
    else:
        print(                 file=file1 )

    # Define gauge-related macros
    # gauge condition type
    # 0: b^i gauge
    # 1: david's puncture gauge
    # 2: mb b^i gauge
    # 3: rit b^i gauge
    # 4: mb beta gauge (beta gauge not means eq.(3) of prd 84, 124006)
    # 5: rit beta gauge (beta gauge not means eq.(3) of prd 84, 124006)
    # 6: mgb1 b^i gauge
    # 7: mgb2 b^i gauge

    if ( input_data.gauge_choice == 0 ):
        print( "#define gauge 0",  file=file1 )
        print(                     file=file1 )
    elif ( input_data.gauge_choice == 1 ):
        print( "#define gauge 1",  file=file1 )
        print(                     file=file1 )
    elif ( input_data.gauge_choice == 2 ):
        print( "#define gauge 2",  file=file1 )
        print(                     file=file1 )
    elif ( input_data.gauge_choice == 3 ):
        print( "#define gauge 3",  file=file1 )
        print(                     file=file1 )
    elif ( input_data.gauge_choice == 4 ):
        print( "#define gauge 4",  file=file1 )
        print(                     file=file1 )
    elif ( input_data.gauge_choice == 5 ):
        print( "#define gauge 5",  file=file1 )
        print(                     file=file1 )
    elif ( input_data.gauge_choice == 6 ):
        print( "#define gauge 6",  file=file1 )
        print(                     file=file1 )
    elif ( input_data.gauge_choice == 7 ):
        print( "#define gauge 7",  file=file1 )
        print(                     file=file1 )
    else:
        print( "gauge setting error!!" )
        print()
        print( "# gauge gauge setting error!!", file=file1 )
        print(                             file=file1 )

    # Define macro cpbc_ghost_width
    # buffer points for cpbc boundary
    
    print( "#define cpbc_ghost_width  (ghost_width)", file=file1 )
    print(                                            file=file1 )

    # Define macro abv
    # 0: use bssn variables for constraint violation and psi4 calculation
    # 1: use adm variables for constraint violation and psi4 calculation
    
    print( "#define abv 0", file=file1 )
    print(                  file=file1 )
    
    # Define macro escalar_cc related to f(r) scalar-tensor theory
    # 1: case c of 1112.3928, v=0
    # 2: shell with   phi(r) = phi0 * a2^2/(1+a2^2), f(r) = r+a2*r^2 induced v
    # 3: ground state of schrodinger-newton system,  f(r) = r+a2*r^2 induced v
    # 4: a2 = +oo and phi(r) = phi0 * 0.5 * ( tanh((r+r0)/sigma) - tanh((r-r0)/sigma) )
    # 5: shell with   phi(r) = phi0 * exp(-(r-r0)**2/sigma), v = 0
    
    if (input_data.equation_class == "bssn-escalar"):
        print( "#define escalar_cc ", input_data.fr_choice, file=file1 )
        print(                                              file=file1 )
    else:
        print( "#define escalar_cc 2",                      file=file1 )
        print(                                              file=file1 )
        # for other calculations this value does not affect results; set a default
        # this prevents errors if fr_choice is not present in config.py
    
    # the following are explanatory comments

    print( "#if 0",                                                                                 file=file1 )
    print(                                                                                          file=file1 )
    print( "define tetradtype",                                                                     file=file1 )
    print( "    v:r; u: phi; w: theta",                                                             file=file1 )
    print( "    tetradtype 0",                                                                      file=file1 )
    print( "    v^a = (x,y,z)",                                                                     file=file1 )
    print( "    orthonormal order: v,u,w",                                                          file=file1 )
    print( "    m = (phi - i theta)/sqrt(2) following frans, eq.(8) of  prd 75, 124018(2007)",      file=file1 )
    print( "    tetradtype 1",                                                                      file=file1 )
    print( "    orthonormal order: w,u,v",                                                          file=file1 )
    print( "    m = (theta + i phi)/sqrt(2) following sperhake, eq.(3.2) of  prd 85, 124062(2012)", file=file1 )
    print( "    tetradtype 2",                                                                      file=file1 )
    print( "    v_a = (x,y,z)",                                                                     file=file1 )
    print( "    orthonormal order: v,u,w",                                                          file=file1 )
    print( "    m = (phi - i theta)/sqrt(2) following frans, eq.(8) of  prd 75, 124018(2007)",      file=file1 )
    print(                                                                                          file=file1 )
    print( "define cell or vertex",                                                                 file=file1 )
    print( "    cell center or vertex center",                                                      file=file1 )
    print(                                                                                          file=file1 )
    print( "define ghost_width",                                                                    file=file1 )
    print( "    2nd order: 2",                                                                      file=file1 )
    print( "    4th order: 3",                                                                      file=file1 )
    print( "    6th order: 4",                                                                      file=file1 )
    print( "    8th order: 5",                                                                      file=file1 )
    print(                                                                                          file=file1 )
    print( "define withshell",                                                                      file=file1 )
    print( "    use shell or not",                                                                  file=file1 )
    print(                                                                                          file=file1 )
    print( "define cpbc",                                                                           file=file1 )
    print( "    use constraint preserving boundary condition or not",                               file=file1 )
    print( "    only affect z4c",                                                                   file=file1 )
    print( "    cpbc only supports withshell",                                                      file=file1 )
    print(                                                                                          file=file1 )
    print( "define gauge",                                                                          file=file1 )
    print( "    0: b^i gauge",                                                                      file=file1 )
    print( "    1: david puncture gauge",                                                           file=file1 )
    print( "    2: mb b^i gauge",                                                                   file=file1 )
    print( "    3: rit b^i gauge",                                                                  file=file1 )
    print( "    4: mb beta gauge (beta gauge not means eq.(3) of prd 84, 124006)",                  file=file1 )
    print( "    5: rit beta gauge (beta gauge not means eq.(3) of prd 84, 124006)",                 file=file1 )
    print( "    6: mgb1 b^i gauge",                                                                 file=file1 )
    print( "    7: mgb2 b^i gauge",                                                                 file=file1 )
    print(                                                                                          file=file1 )
    print( "define cpbc_ghost_width  (ghost_width)",                                                file=file1 )
    print( "    buffer points for cpbc boundary",                                                   file=file1 )
    print(                                                                                          file=file1 )
    print( "define abv",                                                                            file=file1 )
    print( "    0: using bssn variable for constraint violation and psi4 calculation",              file=file1 )
    print( "    1: using adm variable for constraint violation and psi4 calculation",               file=file1 )
    print(                                                                                          file=file1 )
    print( "define escalar_cc",                                                                     file=file1 )
    print( "type of potential and scalar distribution in f(r) scalar-tensor theory",                file=file1 )
    print( "    1: case c of 1112.3928, v=0",                                                       file=file1 )
    print( "    2: shell with   phi(r) = phi0 * a2^2/(1+a2^2), f(r) = r+a2*r^2 induced v",          file=file1 )
    print( "    3: ground state of schrodinger-newton system,  f(r) = r+a2*r^2 induced v",          file=file1 )
    print( "    4: a2 = +oo and phi(r) = phi0 * 0.5 * ( tanh((r+r0)/sigma) - tanh((r-r0)/sigma) )", file=file1 )
    print( "    5: shell with   phi(r) = phi0 * exp(-(r-r0)**2/sigma), v = 0",                      file=file1 )
    print(                                                                                          file=file1 )
    print( "#endif",                                                                                file=file1 )
    print(                                                                                          file=file1 )
    
    file1.close()

    return file1
    
##################################################################

    
```