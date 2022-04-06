TODO:

- [ ] Create `/scripts` dir with poetry files. We'll need `requests` (probably) and `rdflib`, possibly more.
- [ ] Define a list of RDF resources in the form of urls, starting with units catalogue & quantity kinds catalogue as listed for this task.
- Create script that:
     - [ ] Iterates through the above and for each
     - [ ] Gets the RDF resource.
     - [ ] Reads the RDF resources into `rdflib`
     - [ ] Uses `rdflib` to get the identifying url for each thing, i.e `www.url-in-question/something#i-am-a-unit`
     - [ ] Read the appropriate .json file in from this repos base directory and (if the url in question is not already there!) add it to the list in the `enum` field before writing the json file back.

Notes:

Iterating a list of source urls may or may not be appropriate. If its cleaner to do them as separate functions that's fine.

Include a `REAME.md` in the `./scripts` directory explaining what it's doing and how to use it.

Try and write in a DRY way. We'll likely be expanding on sources in time, so organise with that in mind. EG: have a "get data" function, a "convert to rdf" function, some SPARQL queries as constants and an "update json" function. Making use of any given future source should just be a case of composing these things together (and perhaps adding a new SPARQL query variant where needed).