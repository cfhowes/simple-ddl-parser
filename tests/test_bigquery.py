from simple_ddl_parser import DDLParser


def test_dataset_in_output():
    expected = {
        "domains": [],
        "ddl_properties": [],
        "schemas": [],
        "sequences": [],
        "tables": [
            {
                "alter": {},
                "checks": [],
                "columns": [
                    {
                        "check": None,
                        "default": None,
                        "name": "x",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "INT64",
                        "unique": False,
                    }
                ],
                "dataset": "mydataset",
                "index": [],
                "partitioned_by": [],
                "primary_key": [],
                "table_name": "newtable",
                "tablespace": None,
            }
        ],
        "types": [],
    }

    ddl = """
    CREATE TABLE mydataset.newtable ( x INT64 )
    """
    result = DDLParser(ddl).run(group_by_type=True, output_mode="bigquery")
    assert expected == result


def test_simple_struct():
    ddl = """
    CREATE TABLE mydataset.newtable
     (
       x INT64 ,
       y STRUCT<a ARRAY<STRING>,b BOOL>
     )
    """
    parse_results = DDLParser(ddl).run(group_by_type=True, output_mode="bigquery")
    expected = {
        "tables": [
            {
                "columns": [
                    {
                        "name": "x",
                        "type": "INT64",
                        "size": None,
                        "references": None,
                        "unique": False,
                        "nullable": True,
                        "default": None,
                        "check": None,
                    },
                    {
                        "name": "y",
                        "type": "STRUCT < a ARRAY < STRING >, b BOOL >",
                        "size": None,
                        "references": None,
                        "unique": False,
                        "nullable": True,
                        "default": None,
                        "check": None,
                    },
                ],
                "primary_key": [],
                "alter": {},
                "checks": [],
                "index": [],
                "partitioned_by": [],
                "tablespace": None,
                "table_name": "newtable",
                "dataset": "mydataset",
            }
        ],
        "types": [],
        "ddl_properties": [],
        "sequences": [],
        "domains": [],
        "schemas": [],
    }

    assert expected == parse_results
