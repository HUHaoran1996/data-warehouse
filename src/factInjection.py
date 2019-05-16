import pandas as pd
import pymysql
from sqlalchemy import create_engine

def getIndexId(x, data):
    split = data.split(", ")
    keyId = 0;

    for key in split:
        keyId = keyId + 1
        if (key == x):
            return keyId

    return 0;

def main():
    data = pd.read_csv("adult.data", header = None,
                       names=["age", "workclass", "fnlwgt", "education", "education_num", "marital",
                              "occupation", "relationship", "race", "sex", "capital_gain", "capital_loss",
                              "workinghours", "country", "income"], sep = ", ", engine='python')

    data["age"] = data["age"].apply(lambda x: 1 if x < 18 else 2 if x < 35 else 3 if x < 55 else 4)
    data["workinghours"] = data["workinghours"].apply(lambda x: 1 if x < 10 else 2 if x <= 30 else 3 if x <= 40 else 4 if x <= 50 else 5)
    data["income"] = data["income"].apply(lambda x: 1 if x == ">50K" else 2)

    workclass = "Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked"
    data["workclass"] = data["workclass"].apply(lambda x: getIndexId(x, workclass))

    education = "Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, " \
                "1st-4th, 10th, Doctorate, 5th-6th, Preschool"
    data["education"] = data["education"].apply(lambda x: getIndexId(x, education))

    marital = "Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse"
    data["marital"] = data["marital"].apply(lambda x: getIndexId(x, marital))

    occupation = "Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, " \
                 "Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces"
    data["occupation"] = data["occupation"].apply(lambda x: getIndexId(x, occupation))

    relationship = "Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried"
    data["relationship"] = data["relationship"].apply(lambda x: getIndexId(x, relationship))

    race = "White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black"
    data["race"] = data["race"].apply(lambda x: getIndexId(x, race))

    sex = "Female, Male"
    data["sex"] = data["sex"].apply(lambda x: getIndexId(x, sex))

    country = "United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, " \
              "Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, " \
              "Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, " \
              "Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands"
    data["country"] = data["country"].apply(lambda x: getIndexId(x, country))

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

        cursor.execute("DELETE FROM Income_Fact")

        for index, row in data.iterrows():
            insertString = "insert into Income_Fact(userid, ageId, workclassId, fnlwgt, " \
                           "educationId, education_num, maritalId, occupationId, relationshipId, " \
                           "raseId, sexId, capital_gain, capital_loss, workinghoursId, countryId, " \
                           "incomeId) values(\"" + str(index) + "\", \"" + str(row["age"]) + "\", \"" + str(row["workclass"]) + "\", \"" + \
                           str(row["fnlwgt"]) + "\", \""  + str(row["education"]) + "\", \"" + str(row["education_num"]) + "\", \"" + \
                           str(row["marital"]) + "\", \"" + str(row["occupation"]) + "\", \""  + str(row["relationship"]) + "\", \"" \
                           + str(row["race"]) + "\", \"" + str(row["sex"]) + "\", \"" + str(row["capital_gain"]) + "\", \""  + \
                           str(row["capital_loss"]) + "\", \"" + str(row["workinghours"]) + "\", \"" \
                           + str(row["country"]) + "\", \"" + str(row["income"]) + "\")"
            #print(insertString)
            cursor.execute(insertString)


    except:
        import traceback
        traceback.print_exc()
        # 发生错误时会滚
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    #print(data.head())

if __name__ == '__main__':
    main()