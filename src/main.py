import functions
import ontospy
import re 
import os 

# file paths
OWL_PATH_PREFIX = './owl_files'
OBCI_OWL_PATH = f'{OWL_PATH_PREFIX}/obci.owl'
DOID_OWL_PATH = f'{OWL_PATH_PREFIX}/doid.owl'
GLYGEN_OWL_PATH = f'{OWL_PATH_PREFIX}/glygen.owl'

# output file paths
OBCI_OUTPUT_PREFIX = f'./output_files/obci_owl'
DOID_OUTPUT_PREFIX = f'./output_files/doid_owl'

# file types
FILE_TYPES = ['txt', 'csv']

def ontospy_processing():
    ''' Explore the owl files using ontospy. 
    '''

    ### OBCI ###
    obci = ontospy.Ontospy(OBCI_OWL_PATH, hide_individuals = False, verbose = True)

    # explore classes
    functions.ontospy_explore_classes(output_file = f'{OBCI_OUTPUT_PREFIX}/ontospy/classes.txt', classes = obci.all_classes)
    functions.ontospy_explore_classes(output_file = f'{OBCI_OUTPUT_PREFIX}/ontospy/classes.csv', classes = obci.all_classes)
    
    # explore object properties
    functions.ontospy_explore_properties(output_file = f'{OBCI_OUTPUT_PREFIX}/ontospy/object_properties.txt', properties = obci.all_properties_object, property_type = 'object')
    functions.ontospy_explore_properties(output_file = f'{OBCI_OUTPUT_PREFIX}/ontospy/object_properties.csv', properties = obci.all_properties_object, property_type = 'object')

    # explore data properties
    functions.ontospy_explore_properties(output_file = f'{OBCI_OUTPUT_PREFIX}/ontospy/data_properties.txt', properties = obci.all_properties_datatype, property_type = 'data')
    functions.ontospy_explore_properties(output_file = f'{OBCI_OUTPUT_PREFIX}/ontospy/data_properties.csv', properties = obci.all_properties_datatype, property_type = 'data')

    # explore annotation properties
    functions.ontospy_explore_properties(output_file = f'{OBCI_OUTPUT_PREFIX}/ontospy/annotation_properties.txt', properties = obci.all_properties_annotation, property_type = 'annotation')
    functions.ontospy_explore_properties(output_file = f'{OBCI_OUTPUT_PREFIX}/ontospy/annotation_properties.csv', properties = obci.all_properties_annotation, property_type = 'annotation')

    # explore individuals

    ### DOID ###
    doid = ontospy.Ontospy(DOID_OWL_PATH, hide_individuals = False, verbose = True)

    # explore classes
    functions.ontospy_explore_classes(output_file = f'{DOID_OUTPUT_PREFIX}/ontospy/classes.txt', classes = doid.all_classes)



def main():

    ontospy_processing()

if __name__ == '__main__':
    main() 