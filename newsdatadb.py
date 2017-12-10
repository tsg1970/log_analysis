# Python code for the Udacity Log Analysis project

import psycopg2
import pprint

# Create variable for the news database
dbname = "news"


def main():
    """Retrieve data for the most popular 3 articles of all time"""
    db = psycopg2.connect(database=dbname)
    c = db.cursor()

    c.execute("SELECT articles.title, count(*) AS num FROM articles, log WHERE log.path \
            LIKE '%'||articles.slug||'%' \
            GROUP BY articles.title ORDER BY count(*) DESC LIMIT 3")
    records = c.fetchall()
    print("\n" + "The most popular three articles of all time:")
    for record in records:
        print "\t" + str(record[0]) + " -- " + str(record[1]) + " views"

    """Retrieve data for the most popular article authors of all time."""
    c.execute("SELECT authors.name, count(*) AS num FROM articles, log, authors \
            WHERE authors.id = articles.author and \
            log.path LIKE '%'||articles.slug||'%' \
            GROUP BY authors.name ORDER BY count(*) DESC")
    records = c.fetchall()
    print("\n" + "The most popular article authors of all time:")
    for record in records:
        print "\t" + str(record[0]) + " -- " + str(record[1]) + " views"

    """Retrieve data for days of more than 1 pct of requests lead to errors"""
    c.execute("WITH c1_table AS( \
            SELECT to_char(time,'Month DD, YYYY') AS errdate, \
            count((status != '200 OK') OR NULL) AS errcnt, \
            count(*) As total \
            FROM log \
            GROUP BY to_char(time, 'Month DD, YYYY') \
            ORDER BY to_char(time, 'Month DD, YYYY') DESC \
            ), c2_table AS( \
            SELECT errdate, round((errcnt * 100.0) / total, 2) AS errpct \
            FROM c1_table\
            ) \
            SELECT errdate, errpct FROM c2_table WHERE errpct > 1 \
            ")

    records = c.fetchall()
    print("\n" + "Days with more than 1% of requests lead to errors:")
    for record in records:
        print "\t" + str(record[0]) + " -- " + str(record[1]) + "%"


if __name__ == '__main__':
    main()
