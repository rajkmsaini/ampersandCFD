import yaml
from primitives import ampersandPrimitives
from constants import meshSettings, physicalProperties

def create_transportPropertiesDict(transportProperties):
    header = ampersandPrimitives.createFoamHeader(className="dictionary", objectName="transportProperties")
    transportPropertiesDict = f""+header
    transportProperties_ = f"""
transportModel  Newtonian;
nu              nu [ 0 2 -1 0 0 0 0 ] {transportProperties['nu']};
"""
    transportPropertiesDict += transportProperties_
    return transportPropertiesDict

def create_turbulencePropertiesDict(turbulenceProperties):
    header = ampersandPrimitives.createFoamHeader(className="dictionary", objectName="turbulenceProperties")
    turbulencePropertiesDict = f""+header
    turbulenceProperties_ = f"""
simulationType  RAS;
RAS
{{
    RASModel        {turbulenceProperties['turbulenceModel']};
    turbulence      on;
    printCoeffs     on;
    Cmu             0.09;
}}
"""
    turbulencePropertiesDict += turbulenceProperties_
    return turbulencePropertiesDict

def write_transportPropertiesDict(transportPropertiesDict):
    with open('transportProperties', 'w') as file:
        file.write(transportPropertiesDict)

def write_turbulencePropertiesDict(turbulencePropertiesDict):
    with open('turbulenceProperties', 'w') as file:
        file.write(turbulencePropertiesDict)

if __name__ == "__main__":
    transportPropertiesDict = create_transportPropertiesDict(physicalProperties)
    with open('transportProperties', 'w') as file:
        file.write(transportPropertiesDict)
    turbulencePropertiesDict = create_turbulencePropertiesDict(physicalProperties)
    with open('turbulenceProperties', 'w') as file:
        file.write(turbulencePropertiesDict)
    print(transportPropertiesDict)
    print(turbulencePropertiesDict)