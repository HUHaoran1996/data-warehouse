import pymysql

def injectDimensionTable(dimension, table, keyName, cursor):
    splited = dimension.split(", ")

    cursor.execute("DELETE FROM " + table)

    keyId = 0
    #insertString = "insert into "+ table + "("+ keyName + ", textDecs) values(" + str(keyId) + ", \"unknown\")";
    #print(insertString)
    #cursor.execute(insertString)
    for key in splited:
        keyId = keyId + 1;
        insertString = "insert into " + table + "("+ keyName + ", textDecs) values(" + str(keyId) + ", \"" + key +"\")"
        #print(insertString)
        cursor.execute(insertString)

    print("finish inject data to " + table)

def main():
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': '',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }

    conn = pymysql.connect(**config)
    conn.autocommit(1)
    cursor = conn.cursor()

    try:
        # 创建数据库
        DB_NAME = 'INCOMEDB'
        conn.select_db(DB_NAME)

        workclass = "Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked"
        injectDimensionTable(workclass, "WorkClass", "classId", cursor)

        education = "Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, " \
                    "1st-4th, 10th, Doctorate, 5th-6th, Preschool"
        injectDimensionTable(education, "Education", "educationId", cursor)

        marital = "Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse"
        injectDimensionTable(marital, "Marital", "maritalId", cursor)

        occupation = "Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, " \
                     "Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces"
        injectDimensionTable(occupation, "Occupation", "occupationId", cursor)

        relationship = "Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried"
        injectDimensionTable(relationship, "Relationship", "relationshipId", cursor)

        race = "White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black"
        injectDimensionTable(race, "Race", "raceId", cursor)

        sex = "Female, Male"
        injectDimensionTable(sex, "SEX", "sexId", cursor)

        country = "United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, " \
                  "Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, " \
                  "Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, " \
                  "Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands"
        injectDimensionTable(country, "Country", "countryId", cursor)

        age = "Youth, Youth Adult, Adult, Senior"
        injectDimensionTable(age, "Age", "ageId", cursor)

        workinghour = "Few, Little, Middle, More, Large"
        injectDimensionTable(workinghour, "WorkingHours", "workingHoursId", cursor)

        income = "More than 50K, Less than 50K"
        injectDimensionTable(income, "Income", "incomeId", cursor)

    except:
        import traceback
        traceback.print_exc()
        # 发生错误时会滚
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    main()