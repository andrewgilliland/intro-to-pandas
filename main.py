from src import dataframes
from src import read_data
from src import selecting
from src import transforming
from src import grouping
from src import exporting


def main():
    df = dataframes.main()
    read_data.main()
    selecting.main(df)
    df = transforming.main(df)
    grouping.main(df)
    exporting.main(df)


if __name__ == "__main__":
    main()
