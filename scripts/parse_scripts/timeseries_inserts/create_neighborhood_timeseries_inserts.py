def break_into_line_parts(line):
    parts = []
    c_idx = 0
    while c_idx < len(line):
        if line[c_idx] != '"':
            word = ""
            while line[c_idx] != ",":
                word += line[c_idx]
                c_idx += 1
                if c_idx >= len(line):
                    break
            parts.append(word)
            c_idx += 1
        else:
            word = ""
            c_idx += 1
            if c_idx >= len(line):
                break
            while line[c_idx] != '"':
                word += line[c_idx]
                c_idx += 1
            next_idx = c_idx + 1
            if next_idx < len(line):
                if line[next_idx] == ",":
                    c_idx += 2
                else:
                    c_idx += 1
            parts.append(word)

    return parts


def condo():
    insert_lines = []
    month_year_list = []
    with open(
        "data/ZHVI/condoCoOpTimeSeries/Neighborhood_Zhvi_Condominum.csv", "r"
    ) as csv_file:
        line_count = 0
        for line in csv_file:
            line = line.rstrip("\n")
            line_parts = break_into_line_parts(line)
            if line_count == 0:
                month_year_list = line_parts[7:]
                line_count += 1
                continue

            zillow_id = line_parts[0].strip('"')
            neighborhood_name = line_parts[1].strip('"')
            city_name = line_parts[2].strip('"')
            state_code = line_parts[3].strip('"')
            county_name = line_parts[5].strip('"')
            city_name = city_name.replace("'", "''")
            county_name = county_name.replace("'", "''")
            neighborhood_name = neighborhood_name.replace("'", "''")

            home_type_select = "(SELECT id from home_type where type = 'purchase' and feature = 'condoCoOp')"
            neighborhood_select = (
                "(select neighborhood.id from neighborhood "
                "inner join city on neighborhood.city_id = city.id "
                "inner join county on city.county_id = county.id "
                "inner join state on county.state_id = state.id "
                "where neighborhood.name = '"
                + neighborhood_name
                + "' and city.name = '"
                + city_name
                + "' and county.name = '"
                + county_name
                + "' "
                "and state.state_code = '" + state_code + "')"
            )
            for idx in range(7, len(line_parts), 1):
                if line_parts[idx].strip('"') != "":
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "','"
                        + line_parts[idx].strip('"')
                        + "');"
                    )
                else:
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "',null);"
                    )
                insert_lines.append(insert_line)

            line_count += 1

    sql_file = open("data/neighborhood_condoCoOp_timeseries_insert.sql", "a")

    for line in insert_lines:
        sql_file.write(line)
        sql_file.write("\n")

    sql_file.close()


def oneBedroom():
    insert_lines = []
    month_year_list = []

    with open(
        "data/ZHVI/oneBedroomTimeSeries/Neighborhood_Zhvi_1bedroom.csv", "r"
    ) as csv_file:
        line_count = 0
        for line in csv_file:
            line = line.rstrip("\n")
            line_parts = break_into_line_parts(line)
            if line_count == 0:
                month_year_list = line_parts[7:]
                line_count += 1
                continue

            zillow_id = line_parts[0].strip('"')
            neighborhood_name = line_parts[1].strip('"')
            city_name = line_parts[2].strip('"')
            state_code = line_parts[3].strip('"')
            county_name = line_parts[5].strip('"')
            city_name = city_name.replace("'", "''")
            county_name = county_name.replace("'", "''")
            neighborhood_name = neighborhood_name.replace("'", "''")

            # neighborhood_name = neighborhood_name.replace(":", ",")
            home_type_select = "(SELECT id from home_type where type = 'purchase' and feature = 'oneBedroom')"
            neighborhood_select = (
                "(select neighborhood.id from neighborhood "
                "inner join city on neighborhood.city_id = city.id "
                "inner join county on city.county_id = county.id "
                "inner join state on county.state_id = state.id "
                "where neighborhood.name = '"
                + neighborhood_name
                + "' and city.name = '"
                + city_name
                + "' and county.name = '"
                + county_name
                + "' "
                "and state.state_code = '" + state_code + "')"
            )

            for idx in range(7, len(line_parts), 1):
                if line_parts[idx].strip('"') != "":
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "','"
                        + line_parts[idx].strip('"')
                        + "');"
                    )
                else:
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "',null);"
                    )
                insert_lines.append(insert_line)

            line_count += 1

    sql_file = open("data/neighborhood_oneBedroom_timeseries_insert.sql", "a")

    for line in insert_lines:
        sql_file.write(line)
        sql_file.write("\n")

    sql_file.close()


def twoBedroom():
    insert_lines = []
    month_year_list = []

    with open(
        "data/ZHVI/twoBedroomTimeSeries/Neighborhood_Zhvi_2bedroom.csv", "r"
    ) as csv_file:
        line_count = 0
        for line in csv_file:
            line = line.rstrip("\n")
            line_parts = break_into_line_parts(line)
            if line_count == 0:
                month_year_list = line_parts[7:]
                line_count += 1
                continue

            zillow_id = line_parts[0].strip('"')
            neighborhood_name = line_parts[1].strip('"')
            city_name = line_parts[2].strip('"')
            state_code = line_parts[3].strip('"')
            county_name = line_parts[5].strip('"')
            city_name = city_name.replace("'", "''")
            county_name = county_name.replace("'", "''")
            neighborhood_name = neighborhood_name.replace("'", "''")
            # neighborhood_name = neighborhood_name.replace(":", ",")

            home_type_select = "(SELECT id from home_type where type = 'purchase' and feature = 'twoBedroom')"
            neighborhood_select = (
                "(select neighborhood.id from neighborhood "
                "inner join city on neighborhood.city_id = city.id "
                "inner join county on city.county_id = county.id "
                "inner join state on county.state_id = state.id "
                "where neighborhood.name = '"
                + neighborhood_name
                + "' and city.name = '"
                + city_name
                + "' and county.name = '"
                + county_name
                + "' "
                "and state.state_code = '" + state_code + "')"
            )
            for idx in range(7, len(line_parts), 1):
                if line_parts[idx].strip('"') != "":
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "','"
                        + line_parts[idx].strip('"')
                        + "');"
                    )
                else:
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "',null);"
                    )
                insert_lines.append(insert_line)

            line_count += 1

    sql_file = open("data/neighborhood_twoBedroom_timeseries_insert.sql", "a")

    for line in insert_lines:
        sql_file.write(line)
        sql_file.write("\n")

    sql_file.close()


def threeBedroom():
    insert_lines = []
    month_year_list = []

    with open(
        "data/ZHVI/threeBedroomTimeSeries/Neighborhood_Zhvi_3bedroom.csv",
        "r",
        encoding="latin-1",
    ) as csv_file:
        line_count = 0
        for line in csv_file:
            line = line.rstrip("\n")
            line_parts = break_into_line_parts(line)
            if line_count == 0:
                month_year_list = line_parts[7:]
                line_count += 1
                continue

            zillow_id = line_parts[0].strip('"')
            neighborhood_name = line_parts[1].strip('"')
            city_name = line_parts[2].strip('"')
            state_code = line_parts[3].strip('"')
            county_name = line_parts[5].strip('"')
            city_name = city_name.replace("'", "''")
            county_name = county_name.replace("'", "''")
            neighborhood_name = neighborhood_name.replace("'", "''")
            # neighborhood_name = neighborhood_name.replace(":", ",")

            home_type_select = "(SELECT id from home_type where type = 'purchase' and feature = 'threeBedroom')"
            neighborhood_select = (
                "(select neighborhood.id from neighborhood "
                "inner join city on neighborhood.city_id = city.id "
                "inner join county on city.county_id = county.id "
                "inner join state on county.state_id = state.id "
                "where neighborhood.name = '"
                + neighborhood_name
                + "' and city.name = '"
                + city_name
                + "' and county.name = '"
                + county_name
                + "' "
                "and state.state_code = '" + state_code + "')"
            )
            for idx in range(7, len(line_parts), 1):
                if line_parts[idx].strip('"') != "":
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "','"
                        + line_parts[idx].strip('"')
                        + "');"
                    )
                else:
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "',null);"
                    )
                insert_lines.append(insert_line)

            line_count += 1

    sql_file = open("data/neighborhood_threeBedroom_timeseries_insert.sql", "a")

    for line in insert_lines:
        sql_file.write(line)
        sql_file.write("\n")

    sql_file.close()


def fourBedroom():
    insert_lines = []
    month_year_list = []

    with open(
        "data/ZHVI/fourBedroomTimeSeries/Neighborhood_Zhvi_4bedroom.csv", "r"
    ) as csv_file:
        line_count = 0
        for line in csv_file:
            line = line.rstrip("\n")
            line_parts = break_into_line_parts(line)
            if line_count == 0:
                month_year_list = line_parts[7:]
                line_count += 1
                continue

            zillow_id = line_parts[0].strip('"')
            neighborhood_name = line_parts[1].strip('"')
            city_name = line_parts[2].strip('"')
            state_code = line_parts[3].strip('"')
            county_name = line_parts[5].strip('"')
            city_name = city_name.replace("'", "''")
            county_name = county_name.replace("'", "''")
            neighborhood_name = neighborhood_name.replace("'", "''")
            # neighborhood_name = neighborhood_name.replace(":", ",")

            home_type_select = "(SELECT id from home_type where type = 'purchase' and feature = 'fourBedroom')"
            neighborhood_select = (
                "(select neighborhood.id from neighborhood "
                "inner join city on neighborhood.city_id = city.id "
                "inner join county on city.county_id = county.id "
                "inner join state on county.state_id = state.id "
                "where neighborhood.name = '"
                + neighborhood_name
                + "' and city.name = '"
                + city_name
                + "' and county.name = '"
                + county_name
                + "' "
                "and state.state_code = '" + state_code + "')"
            )
            for idx in range(7, len(line_parts), 1):
                if line_parts[idx].strip('"') != "":
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "','"
                        + line_parts[idx].strip('"')
                        + "');"
                    )
                else:
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "',null);"
                    )
                insert_lines.append(insert_line)

            line_count += 1

    sql_file = open("data/neighborhood_fourBedroom_timeseries_insert.sql", "a")

    for line in insert_lines:
        sql_file.write(line)
        sql_file.write("\n")

    sql_file.close()


def fivePlusBedroom():
    insert_lines = []
    month_year_list = []

    with open(
        "data/ZHVI/fivePlusBedroomTimeSeries/Neighborhood_Zhvi_5BedroomOrMore.csv", "r"
    ) as csv_file:
        line_count = 0
        for line in csv_file:
            line = line.rstrip("\n")
            line_parts = break_into_line_parts(line)
            if line_count == 0:
                month_year_list = line_parts[7:]
                line_count += 1
                continue

            zillow_id = line_parts[0].strip('"')
            neighborhood_name = line_parts[1].strip('"')
            city_name = line_parts[2].strip('"')
            state_code = line_parts[3].strip('"')
            county_name = line_parts[5].strip('"')
            city_name = city_name.replace("'", "''")
            county_name = county_name.replace("'", "''")
            neighborhood_name = neighborhood_name.replace("'", "''")
            # neighborhood_name = neighborhood_name.replace(":", ",")

            home_type_select = "(SELECT id from home_type where type = 'purchase' and feature = 'fivePlusBedroom')"
            neighborhood_select = (
                "(select neighborhood.id from neighborhood "
                "inner join city on neighborhood.city_id = city.id "
                "inner join county on city.county_id = county.id "
                "inner join state on county.state_id = state.id "
                "where neighborhood.name = '"
                + neighborhood_name
                + "' and city.name = '"
                + city_name
                + "' and county.name = '"
                + county_name
                + "' "
                "and state.state_code = '" + state_code + "')"
            )
            for idx in range(7, len(line_parts), 1):
                if line_parts[idx].strip('"') != "":
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "','"
                        + line_parts[idx].strip('"')
                        + "');"
                    )
                else:
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "',null);"
                    )
                insert_lines.append(insert_line)

            line_count += 1

    sql_file = open("data/neighborhood_fivePlusBedroom_timeseries_insert.sql", "a")

    for line in insert_lines:
        sql_file.write(line)
        sql_file.write("\n")

    sql_file.close()


def singleFamilyHome():
    insert_lines = []
    month_year_list = []

    with open(
        "data/ZHVI/singleFamilyHomeTimeSeries/Neighborhood_Zhvi_SingleFamilyResidence.csv",
        "r",
        encoding="latin-1",
    ) as csv_file:
        line_count = 0
        for line in csv_file:
            line = line.rstrip("\n")
            line_parts = break_into_line_parts(line)
            if line_count == 0:
                month_year_list = line_parts[7:]
                line_count += 1
                continue

            zillow_id = line_parts[0].strip('"')
            neighborhood_name = line_parts[1].strip('"')
            city_name = line_parts[2].strip('"')
            state_code = line_parts[3].strip('"')
            county_name = line_parts[5].strip('"')
            city_name = city_name.replace("'", "''")
            county_name = county_name.replace("'", "''")
            neighborhood_name = neighborhood_name.replace("'", "''")
            # neighborhood_name = neighborhood_name.replace(":", ",")

            home_type_select = "(SELECT id from home_type where type = 'purchase' and feature = 'singleFamilyHome')"
            neighborhood_select = (
                "(select neighborhood.id from neighborhood "
                "inner join city on neighborhood.city_id = city.id "
                "inner join county on city.county_id = county.id "
                "inner join state on county.state_id = state.id "
                "where neighborhood.name = '"
                + neighborhood_name
                + "' and city.name = '"
                + city_name
                + "' and county.name = '"
                + county_name
                + "' "
                "and state.state_code = '" + state_code + "')"
            )
            for idx in range(7, len(line_parts), 1):
                if line_parts[idx].strip('"') != "":
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "','"
                        + line_parts[idx].strip('"')
                        + "');"
                    )
                else:
                    insert_line = (
                        "INSERT INTO neighborhood_timeseries (neighborhood_id, home_type_id, year_month, zillow_id, index_value)"
                        + " VALUES("
                        + neighborhood_select
                        + ","
                        + home_type_select
                        + ",'"
                        + month_year_list[idx - 7].strip('"')
                        + "','"
                        + zillow_id
                        + "',null);"
                    )
                insert_lines.append(insert_line)

            line_count += 1

    sql_file = open(
        "data/neighborhood_singleFamilyResidence_timeseries_insert.sql", "a"
    )

    for line in insert_lines:
        sql_file.write(line)
        sql_file.write("\n")

    sql_file.close()


condo()
oneBedroom()
twoBedroom()
threeBedroom()
fourBedroom()
fivePlusBedroom()
singleFamilyHome()
