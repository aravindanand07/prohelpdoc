***************************************
Example Command File
***************************************

Here is a sample command parameters file (it can be downloaded :download:`here <media/vmcae_input_sample>`)::

    #############################################################################
    #                                                                           #
    #                     VMoveCAESubmit Input file                             #
    #                                                                           #
    #############################################################################
    #                                                                           #
    # The translation inputs are categorized into different sections.           #
    #                                                                           #
    # Section lines start with "* "                                             #
    # Data lines start with "- ".                                               #
    #                                                                           #
    #############################################################################
    #                                                                           #
    # FILES Section                                                             #
    # -------------                                                             #
    #                                                                           #
    #   This section specifies all the files that needs to be read into         #
    #   VMoveCAE. This is a mandatory section.                                  #
    #                                                                           #
    #   Usage Example:                                                          #
    #   -------------                                                           #
    #                                                                           #
    #     * FILES, FOLDER="/home/vcollab/models"                                #
    #     - "viewer_tutorial.odb", TYPE=ODB                                     #
    #                                                                           #
    #    File names are specified in the data lines. File names can be          #
    #    enclosed in quotes if they contain spaces or any special characters.   #
    #                                                                           #
    #  Section Options:                                                         #
    #  ---------------                                                          #
    #                                                                           #
    #    FOLDER: Base folder. When a base folder is specified, all the relative #
    #            paths are considered to be relative to the base folder.        #
    #                                                                           #
    #  Data Options:                                                            #
    #  -------------                                                            #
    #                                                                           #
    #    TYPE: File type. Supported values are:                                 #
    #          - ABAQUS_ODB                                                     #
    #          - ABAQUS_INP                                                     #
    #          - FEMFAT_UFF                                                     #
    #          - NCODE                                                          #
    #          If not specified, VMoveCAE tries to auto-detect the file type.   #
    #    CONTENT: Tells VMoveCAE what to read from specific file. If not        #
    #             specified, VMoveCAE handles it automaticaly.                  #
    #             Supported values are:                                         #
    #             - MODEL                                                       #
    #             - ENTITY_SETS                                                 #
    #             - RESULTS                                                     #
    #                                                                           #
    #############################################################################
    
    * FILES, FOLDER="/home/vcollab/models"
    
    - viewer_tutorial.inp, TYPE=ABAQUS_INP, CONTENT=ENTITY_SETS
    - viewer_tutorial.odb, TYPE=ABAQUS_ODB, CONTENT="MODEL, RESULTS"
    - viewer_tutorial.cax, TYPE=VCOLLAB
    
    #############################################################################
    #                                                                           #
    # PARTS Section                                                             #
    # -------------                                                             #
    #                                                                           #
    #   This section tells VMoveCAE how to group elements into parts, what      #
    #   parts to translate and what parts to filter. This is an optional        #
    #   section. If not specified, VMoveCAE uses default part grouping          #
    #   element sets for Abaqus models) and exports all parts into the          #
    #   CAX file.                                                               #
    #                                                                           #
    #   Usage Example:                                                          #
    #   -------------                                                           #
    #                                                                           #
    #     * PARTS, GROUPING=element-set                                         #
    #     - STD*, FILTER                                                        #
    #     - HB*                                                                 #
    #                                                                           #
    #    Part names are specified in the data lines. Part names can be          #
    #    enclosed in quotes if they contain spaces or any special characters.   #
    #                                                                           #
    #  Section Options:                                                         #
    #  ---------------                                                          #
    #                                                                           #
    #    GROUPING: Part grouping to be used. Supported values:                  #
    #              - property-id                                                #
    #              - material-id                                                #
    #              - element-set                                                #
    #              - element-and-face-sets                                      #
    #                                                                           #
    #  Data Options:                                                            #
    #  -------------                                                            #
    #                                                                           #
    #    FILTER: Filters the part from Cax output.                              #
    #                                                                           #
    #############################################################################
    
    * PARTS, GROUPING=element-and-face-sets
    
    - STD*, FILTER
    - _Whole*, FILTER
    - *TETRA_MESH*, FILTER
    - "_ALL ELEMENTS", FILTER
    - *WarnElem*, FILTER
    
    #- Part*
    
    
    #############################################################################
    #                                                                           #
    # RESULTS Section                                                           #
    # ---------------                                                           #
    #                                                                           #
    #   This section tells VMoveCAE what results to translate and what results  #
    #   to filter. This is an optional section. If not specified, VMoveCAE      #
    #   exports all results into the CAX file.                                  #
    #                                                                           #
    #   Usage Example:                                                          #
    #   -------------                                                           #
    #                                                                           #
    #     * RESULTS                                                             #
    #     - Displacement, SOURCE=U                                              #
    #     - NT                                                                  #
    #     - Stress, SOURCE=S, THRESHOLD=75                                      #
    #     - Elemental Stress, SOURCE=S, POSITION=E                              #
    #                                                                           #
    #    Result names are specified in the data lines. Result names can be      #
    #    enclosed in quotes if they contain spaces or any special characters.   #
    #    Alternately, users can specify the source result name in the native    #
    #    CAE solver instead of using VCollab result name.                       #
    #                                                                           #
    #  Data Options:                                                            #
    #  -------------                                                            #
    #                                                                           #
    #    FILTER: Filters the result from Cax output.                            #
    #    SOURCE: Name of the variable as specified by CAE solver                #
    #    POSITION: Whether the Cax file should provide nodal (N) or             #
    #              elemental (E) values.                                        #
    #    DERIVED: Name of the derived component that needs to be extracted      #
    #    THRESHOLD: Percentage of averaging threshold to be used (similar to    #
    #               Abaqus viewer)                                              #
    #                                                                           #
    #############################################################################
    
    * RESULTS
    #- U
    #- S, DERIVED=VON_MISES, THRESHOLD=75
    #- S, DERIVED=MAX_PRINCIPAL, THRESHOLD=75
    #- S, DERIVED=MIN_PRINCIPAL
    #- S, DERIVED=XX, POSITION=E
    #- E
    #- *cont*pres*
    # - PEEQ
    
    #############################################################################
    #                                                                           #
    # STEPS Section                                                             #
    # -------------                                                             #
    #                                                                           #
    #   This section tells VMoveCAE what instances to translate and what        #
    #   instances to filter. This is an optional section. If not specified,     #
    #   VMoveCAE exports all instances into the CAX file.                       #
    #                                                                           #
    #   Usage Example:                                                          #
    #   -------------                                                           #
    #                                                                           #
    #     * STEPS                                                               #
    #     - STEP=1:100:10, INCREMENT=-1                                         #
    #                                                                           #
    #    Step numbers are specified in the data lines. A range can be be        #
    #    specified using ":" as a separator. "-1" can be used to refer to the   #
    #    last step. "ALL" refers to all the available steps.                    #
    #                                                                           #
    #  Data Options:                                                            #
    #  -------------                                                            #
    #                                                                           #
    #    STEP: Step numbers are specified in the data lines. A range can be be  #
    #          specified using ":" as a separator. "-1" can be used to refer to #
    #          the last step. "ALL" refers to all the available steps.          #
    #    INCREMENT: Increment number of the step to translate. A range can be   #
    #               be specified using ":" as a separator. "-1" can be used to  #
    #               refer to the last increment.                                #
    #    TIME: Time of the step/frame that needs to be translated.              #
    #    FREQUENCY: Frequency of the step/frame that needs to be translated.    #
    #                                                                           #
    #############################################################################
    
    #* STEPS
    #- STEP=2, INCREMENT=4:10

