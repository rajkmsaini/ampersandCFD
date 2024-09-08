import os
import yaml

class ampersandPrimitives:
    def __init__(self):
        pass

    @staticmethod
    def dict_to_yaml(data, output_file):
        """
        Convert a dictionary to a YAML file.

        Parameters:
        - data (dict): The dictionary to be converted.
        - output_file (str): The name of the output YAML file.
        """
        with open(output_file, 'w') as file:
            yaml.dump(data, file, default_flow_style=False, sort_keys=False)
        print(f"YAML file '{output_file}' has been created.")


    @staticmethod
    def yaml_to_dict(input_file):
        """
        Read a YAML file and convert it to a dictionary.

        Parameters:
        - input_file (str): The name of the input YAML file.

        Returns:
        - dict: The dictionary representation of the YAML file.
        """
        with open(input_file, 'r') as file:
            data = yaml.safe_load(file)
        return data

    @staticmethod
    # This file contains the basic primitives used in the generation of OpenFOAM casefiles
    def createFoamHeader(className="dictionary",objectName="blockMeshDict"):
        header = f"""/*----------------------------*- AmpersandCFD -*------------------------------*\ 
/*--------------------------------*- C++ -*----------------------------------*\         
| ========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2312                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/

/*This file is part of OpenFOAM casefiles automatically generated by AmpersandCFD*/
FoamFile
{{
    version     2.0;
    format      ascii;
    class       {className};
    object      {objectName};
}}"""
        return header

    @staticmethod
    def createDimensions(M=1,L=1,T=1):
        return f"\ndimensions      [{M} {L} {T} 0 0 0 0];"
    
    @staticmethod
    def createInternalFieldScalar(type="uniform",value=0):
        return f"""\ninternalField   {type} {value};"""
    
    @staticmethod
    def createInternalFieldVector(type="uniform",value=(0,0,0)):
        return f"""\ninternalField   {type} ({value[0]} {value[1]} {value[2]});"""

    @staticmethod
    def write_to_file(filename, content):
        with open(filename, 'w') as f:
            f.write(content)
    @staticmethod
    def createScalarFixedValue(patch_name="inlet",value=0):
        return f"""\n{patch_name}
        {{
            type            fixedValue;
            value           uniform {value};
        }};"""

    @staticmethod
    def createScalarZeroGradient(patch_name="inlet"):
        return f"""\n{patch_name}
        {{
            type            zeroGradient;
        }};"""

    @staticmethod
    def createVectorFixedValue(patch_name="inlet",value=[0,0,0]):
        return f"""\n{patch_name}
        {{
            type            fixedValue;
            value           uniform ("{value[0]} {value[1]} {value[2]})";
        }};""" 

    @staticmethod
    def createVectorZeroGradient(patch_name="inlet"):
        return f"""\n{patch_name}
        {{
            type            zeroGradient;
        }};"""
    
    @staticmethod
    def write_dict_to_file(filename, content):
        with open(filename, 'w') as f:
            f.write(content)

if __name__ == "__main__":
    print(ampersandPrimitives.createFoamHeader(className="dictionary",objectName="snappyHexMeshDict"))
    print(ampersandPrimitives.createDimensions(M=1,L=1,T=1))
    print(ampersandPrimitives.createScalarFixedValue(patch_name="inlet",value=0))
    print(ampersandPrimitives.createScalarZeroGradient(patch_name="inlet"))
    print(ampersandPrimitives.createVectorFixedValue(patch_name="inlet",value=[0,0,0]))



