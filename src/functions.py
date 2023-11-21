from owlready2 import *

### owlready2 based functions 

def or2_explore_classes(output_file: str, classes: list) -> None:
    ''' Explore the ontology classes and writes the data to a text file.

    Parameters
    ----------
    output_file: str
        Where to send the output information.
    classes: list
        List of the classes to parse from owlready2.
    '''

    with open(output_file, 'w') as f:
        for cls in classes:
            f.write(f'CLASS: {cls}\n')
            f.write(f'\tNAME:           {cls.name}\n')
            f.write(f'\tLABEL:          {cls.label}\n')
            f.write(f'\tPARENT:         {cls.is_a}\n')
            f.write(f'\tIRI:            {cls.iri}\n')
            f.write(f'\tSTORID:         {cls.storid}\n')
            f.write(f'\tNAMESPACE:      {cls.namespace}\n')
            f.write(f'\tANNOTATIONS:\n')
            for idx, annotation in enumerate(cls.comment):
                f.write(f'\t\tAnnotation #{idx + 1}: {annotation}\n')
            f.write(f'\n')

def explore_properties(output_file: str, properties: list, property_type: str) -> None:
    ''' Explore the data or object properties and write the data to a text file.

    Parameters
    ----------
    output_file: str
        Where to send the output information. 
    properties: list
        List of the properties to parse from owlready2.
    property_type: str
        Whether the properties being parsed are object or data properties. 
    '''

    with open(output_file, 'w') as f:
        for property in properties:
            f.write(f'{property_type.upper()} PROPERTY: {property}\n')
            f.write(f'\tLABEL:      {property.label}\n')
            f.write(f'\tIRI:        {property.iri}\n')
            f.write(f'\t DOMAIN:    {property.domain}\n')
            f.write(f'\tRANGE:      {property.range}')