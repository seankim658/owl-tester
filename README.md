# Ontology Exploration 

Simple repository for exploring ontology owl files. 

## Supplemental Information 

- [RDF Triples and Ontologies](#rdf-triples-and-ontologies)
- [Ontology Componenets](#ontology-components)
    - [Class](#class)
- [Supplementary Glossary](#supplementary-glossary)

### RDF Triples and Ontologies

When working with ontologies and creating RDF triples, you should reuse existing terms (subjects, predicates, objects) whenever they are available and appropriate for your data, rather than creating new ones. This practice promotes data interoperability and makes your data more easily integrated with other datasets. 

How to approach this:
1. **Check Standard Vocabularies**: For many domains, there are established vocabularies nad ontologies with URIs for a wide range of concepts. For instance, you would use the Disease Ontology (DOID) to reference diseases. If you have a disease identifier, you would use the existing DOID URI as the object in your triple rather than creating a new URI. 

2. **Use Ontology Browsers/Repositories**: Tools like BioPortal, Ontobee, or the OBO Foundry provide browsers for existing ontologies. You can search for terms or concepts and find out if there is already an IRI that represents the concept you want to use.

3. **Follow Namsepace Conventions**: When reusing terms from external vocabularies, you should adhere to their namespace conventions. For instance, if you're using a DOID ID, your object will look like http://purl.obolibrary.org/obo/DOID_XXXX, where XXXX is the specific disease identifier.

4. **Reuse Across Your Data**: Ensure consistency within your own dataset. If you reference a concept once, always use the same URI for that concept elsewhere in your data.

5. **Query External Sources**: If you have access to a SPARQL endpoint for the ontology or a linked data service, you can query it to check if a concept exists before creating a new one. You can also retrieve the owl file and explore it using this repository. 

6. **Use Ontology Management Tools**: Tools like Protégé or this repository can help you explore existing ontologies that you have included in your ontology environment.

7. **Document URIs**: Keep documentation of the URIs you use, especially when you start creating new ones, to prevent duplication in the future.

When creating RDF triples, if you reference external terms like DOID IDs, you would typically do something like this:


```
@prefix doid: <http://purl.obolibrary.org/obo/>.

<http://example.org/your_data#someIndividual> a <http://example.org/your_ontology#YourClass> .
<http://example.org/your_data#someIndividual> <http://example.org/your_ontology#hasDisease> doid:DOID_XXXX .
```

In this example, someIndividual is an instance of YourClass and is associated with a disease that has an identifier DOID_XXXX. The predicate hasDisease would be defined in your ontology, but the object is the existing DOID ID.

Remember to replace `http://example.org/your_ontology#YourClass` and `http://example.org/your_ontology#hasDisease` with actual URIs from your ontology, and DOID_XXXX with the actual DOID identifier.


### Ontology Components

#### Class

**Background and Definition**: In the context of ontologies, a **class** is a fundamental concept that plays a crucial role in structuring and defining the knowledge domain represented by the ontology. The definition of a class is a category or group of things that share common characteristics. It represents a concept or a type of object within the domain of the ontology.

**Organization**: Classes are often organized hierarchically. A more general class can have more specific subclasses. This hierarchical organization allows for the creation of a taxonomy within the ontology, where broader concepts encompass more specific ones.

**Example**: Consider an ontology about living organisms. In this ontology, 'Mammal' might be a class. Under this class, there can be subclasses like 'Primate', 'Carnivore', etc. Further, under 'Primate', there could be classes like 'Human', 'Chimpanzee', etc. Each of these classes represents a concept with specific characteristics that define members of that class.

**Properties and Relationships**: Classes can have properties (also known as attributes) that describe the characteristics of the class. For instance, the class 'Bird' might have properties like 'has wings' or 'can fly'. Classes are also involved in relationships with other classes, which describe how instances of one class relate to instances of another class.

**Instances**: An instance (or individual) in an ontology is a specific example of a class. For instance, in an ontology where 'Car' is a class, a specific car like 'My Honda Civic' would be an instance of the 'Car' class.

**Semantic Web and RDF**: In the Semantic Web, classes are often defined using RDF Schema (RDFS) or Web Ontology Language (OWL), which provide frameworks for describing classes and their relationships in a machine-readable format. In terms of RDF triples, classes can represent either subjects or objects. 

### Supplementary Glossary 

- **IRI**: The term IRI stands for International Resource Identifier. It is a generalization of the more familiar URL (Uniform Reource Locator) and URI (Uniform Resource Identifier). While URLs and URIs are limited to a subset of the ASCII character set, IRIs can include characters from the Universal Character Set (Unicode/ISO 10646), which includes characters from most of the written languages in use on computers today. This makes IRIs more globally accessible because they can contain characters such as those from the Cyrillic, Chinese, Arabic, and Hindi scripts, among others. In the context of semantic web technologies, including RDF and OWL, the term IRI is used because these standards are designed to be international and to support a global, multilingual web.

- **Ontology**: In the context of computer and information science, an ontology refers to a formal representation of knowledge as a set of conceptss within a domain, and the relationships between those concepts. It's used to model a domain of knowledge or a particular topic by defining a set of concepts and categories that represent the domain and by specifying the relationships between these concepts.

- **RDF Triple**: An RDF (Resource Description Framework) triple is a fundamental concept in the context of ontologies, particularly in the realm of the Semantic Web and data representation. It plays a crucial role in how knowledge and relationships are structured and understood in these systems. In RDF triples, the components — *subjects*, *predicates*, and *objects* — are typically represented using URIs (Uniform Resource Identifiers). This use of URIs allows RDF triples to unambiguously refer to specific entities and relationships, facilitating data integration, linking, and querying across diverse data sources on the web. It's a fundamental part of how RDF supports the Semantic Web's goal of making data machine-readable and semantically rich. Here's a breakdown of what an RDF triple is and its relation to ontologies:

    1. **Basic Structure**: An RDF triple consists of three components:

        - **Subject**: The entity or concept being described.
        - **Predicate**: The relationship or property that connects the subject to the object.
        - **Object**: The value or another entity that is related to the subject through the predicate.  
    
    2. **Semantic Web**: RDF is a key technology in the Semantic Web, which aims to make data on the Internet machine-readable and understandable. Ontologies provide the vocabulary and structure, while RDF triples are the means of expressing specific pieces of data or knowledge according to that structure.

    3. **Interlinking Data**: RDF triples allow for easy interlinking of data from different sources. Since RDF uses URIs (Uniform Resource Identifiers) for subjects and predicates, it can easily link data across different datasets and domains.

    4. **Flexibility and Extendibility**: RDF's simple triple structure is both flexible and extendible, making it suitable for representing complex relationships in data. It can be expanded with additional triples to add more detail or to link related concepts.