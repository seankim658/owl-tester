# from owlready2 import *
import csv

### ontospy functions ### 




### owlready2 functions (DEPRECATED, if using these expect issues) ### 

def _get_output_type(output_path: str) -> str:
    ''' Get the output file type from the output_path.

    Parameters
    ----------
    output_path: str 
        The user inputted output_path. 
    '''
    if output_path.endswith('.txt'):
        return 'txt'
    elif output_path.endswith('.csv'):
        return 'csv'
    else:
        raise ValueError(f'Unsupported file type.')

### owlready2 based functions 

def or2_explore_classes(output_file: str, classes: list) -> None:
    ''' Explore the ontology classes and writes the data to an output file. Supports
    txt and csv files. 

    Parameters
    ----------
    output_file: str
        Where to send the output information.
    classes: list
        List of the classes to parse from owlready2.
    '''

    output_type = _get_output_type(output_file)

    if output_type == 'txt':
        with open(output_file, 'w') as f:
            for idx, cls in enumerate(classes):
                f.write(f'CLASS #{idx + 1}: {cls}\n\n')
                f.write(f'\tNAME:           {cls.name}\n')
                f.write(f'\tLABEL:          {cls.label}\n')
                f.write(f'\tPARENT:         {cls.is_a}\n')
                f.write(f'\tIRI:            {cls.iri}\n')
                f.write(f'\tSTORID:         {cls.storid}\n')
                f.write(f'\tNAMESPACE:      {cls.namespace.base_iri}\n')
                f.write(f'\tANNOTATIONS:\n')
                for idx, annotation in enumerate(cls.comment):
                    f.write(f'\t\tAnnotation #{idx + 1}: {annotation}\n')
                f.write(f'\n')
    elif output_type == 'csv':
        with open(output_file, 'w', newline = '') as f:
            writer = csv.writer(f)
            writer.writerow(['class', 'name', 'label', 'parent', 'iri', 'storid', 'namespace', 'annotations'])
            for cls in classes:
                annotations = [f'Annotation #{idx + 1}: {annotation}' for idx, annotation in enumerate(cls.comment)]
                writer.writerow([cls, cls.name, cls.label, cls.is_a, cls.iri, cls.storid, cls.namespace.base_iri] + annotations)

def explore_properties(output_file: str, properties: list, property_type: str) -> None:
    ''' Explore the data or object properties and write the data to an output file. Supports 
    txt and csv files.

    Parameters
    ----------
    output_file: str
        Where to send the output information. 
    properties: list
        List of the properties to parse from owlready2.
    property_type: str
        Whether the properties being parsed are object, data, or annotation properties or all properties (accepts 'object', 'data', 'annotation', 'all').
    '''

    output_type = _get_output_type(output_file)

    if output_type == 'txt':
        with open(output_file, 'w') as f:
            for idx, property in enumerate(properties):
                if property_type == 'all':
                    f.write(f'PROPERTY #{idx + 1}: {property}\n\n')
                elif property_type == 'data' or property_type == 'object' or property_type == 'annotation':
                    f.write(f'{property_type.upper()} PROPERTY #{idx + 1}: {property}\n\n')
                f.write(f"\tLABEL:          {getattr(property, 'label', 'Not Specified')}\n")
                f.write(f"\tIRI:            {getattr(property, 'iri', 'Not specified')}\n")
                f.write(f"\tDOMAIN:         {getattr(property, 'domain', 'Not specified')}\n")
                f.write(f"\tRANGE:          {getattr(property, 'range', 'Not specified')}\n")
                f.write(f"\tCOMMENT:        {getattr(property, 'comment', 'Not specified')}\n\n")
    elif output_type == 'csv':
        with open(output_file, 'w', newline = '') as f:
            writer = csv.writer(f)
            if property_type == 'all':
                writer.writerow([f'property', 'label', 'iri', 'domain', 'range', 'comment'])
            elif property_type == 'data' or property_type == 'object' or property_type == 'annotation':
                writer.writerow([f'{property_type}_property', 'label', 'iri', 'domain', 'range', 'comment'])
            for property in properties:
                writer.writerow([property, property.label, property.iri, property.domain, property.range, property.comment])

def explore_individuals(output_file: str, individuals: list) -> None:
    ''' Explore the ontology defined individuals and write the data to an output file. Supports 
    txt and csv files.

    Parameters
    ----------
    output_file: str
        Where to send the output information.
    individuals: list
        List of the individuals to parse from owlready2. 
    '''

    output_type = _get_output_type(output_file)

    if output_type == 'txt':
        with open(output_file, 'w') as f:
            for idx, individual in enumerate(individuals):
                f.write(f'INDIVIDUAL: {individual}\n\n')
                f.write(f'\tNAME      {individual.name}\n')
                f.write(f'\tLABEL:    {individual.label}\n')
                f.write(f'\tIRI:      {individual.iri}\n\n')
    elif output_type == 'csv':
        with open(output_file, 'w', newline = '') as f:
            writer = csv.writer(f)
            writer.writerow(['individual', 'name', 'label', 'iri'])
            for individual in individuals:
                writer.writerow([individual, individual.name, individual.label, individual.iri])