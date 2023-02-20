# Reusable Measures

These hierarchical measures are designed to aide with the comparisons of measures on the hierarchy; it may be inferred that proximity between nodes denotes a form of similarity.

## Notes on use

It is suggested that these measures not be used directly, but used as a parent measure for any produced data set. For example, the "Ambulance Response Time" measure should be the parent of the measure contained in a data set called "Northern Ireland Ambulance Response Time by Local Government Area". This allows for another data set such as "England Ambulance Response Times by NHS Trust Area" to have the same parent; however as both children will have differing methods of calculating the response times these two measures are comparable for most purposes so their proximity on the hierarchy allows for comparison between the two measures' observations. 

*If you are using a measure from these resources without an assigned `data_type` you cannot use this resource directly.* This is because a measure resource without a `data_type` would break RDF Data Cube Vocabulary constraints.

## Draft measures, relationship exploration

This is currently a non-versioned hiearchy as such the resources are subject to change. The intent is that every node will remain addressable as these measures are created/discovered; however they may be reorganised in a way where a node's location with the hiearchy may change.

The draft hierarchy can be found [on Miro](https://miro.com/app/board/uXjVPco-cCs=/?share_link_id=366659006253). Resources in grey have not been created, and resources in brackets are not meant to be used directly. The promise of keeping resources regardless of reoganisation does not apply to resources in brackets.

e.g. the resource #herds right now is a child of #animal-population, #herds may be moved up a level to a child of #population at a later date but #herds will remain addressable regardless.

## Using these measures

Take the value the in the "identifier" column for the measure you want to use with the prefix `https://purl.org/csv-cubed/resources/measures`, e.g. `https://purl.org/csv-cubed/resources/measures#people`.
