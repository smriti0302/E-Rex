from neo4j import GraphDatabase,exceptions
# from app.utils.secretHandler import getSecret

class Database:
    def __init__(self):
        try:
            uri="bolt://localhost:7687"
            # username = getSecret(['neo4jdb','username'])
            # password = getSecret(['neo4jdb','password'])
            # username = getSecret(['testdb','username'])
            # password = getSecret(['testdb','password'])
            username = "neo4j"
            password = "erex,12345"
            self._driver=GraphDatabase.driver(uri,auth=(username,password))
            self._driver.verify_connectivity()
            print("Neo4j Driver working!") 
            self._session=None
        except exceptions.Neo4jError as e:
            print("Neo4j error:", e)
        except Exception as e:
            print("An error occurred:", e)
    
    def close(self):
        self._driver.close()

    def getSession(self):
        try:
            if(self._session is None):
                print("Opening a new session!")
                self._session=self._driver.session()
                return self._session
            else:
                return self._session
        except exceptions.Neo4jError as e:
            print("Neo4j error:", e)
        except Exception as e:
            print("An error occurred:", e)

    def closeSession(self):
        self._session=self._session.close()