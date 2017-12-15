#! /usr/bin/env python3

# Python code for the Udacity Log Analysis project

import psycopg2
import pprint


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("There was an error accessing the database")


def poparticles():
    """Retrieve data for the most popular 3 articles of all time"""
    db, cursor = connect()
    query = "SELECT title, count(*) AS views \
        FROM log join articles \
        on log.path = concat('/article/', articles.slug) \
        group by title \
        order by views DESC \
        limit 3"
    cursor.execute(query)
    records = cursor.fetchall()
    db.close()
    print("\n" + "The most popular three articles of all time:")
    for record in records:
        print "\t" + str(record[0]) + " -- " + str(record[1]) + " views"


def popauthors():
    """Retrieve data for the most popular article authors of all time."""
    db, cursor = connect()
    query = "SELECT name, count(*) AS views \
        FROM log join articles \
        on log.path = concat('/article/', articles.slug) \
        join authors \
        ON authors.id =  articles.author \
        group by authors.name \
        order by views DESC"
    cursor.execute(query)
    records = cursor.fetchall()
    db.close()
    print("\n" + "The most popular article authors of all time:")
    for record in records:
        print "\t" + str(record[0]) + " -- " + str(record[1]) + " views"


def requesterr():
    """Retrieve data for days of more than 1 pct of requests lead to errors"""
    db, cursor = connect()
    query = "SELECT to_char(date, 'FMMonth FMDD, YYYY'),\
        errcnt/total* 100 AS ratio\
        FROM (SELECT time::date AS date,\
        count(*) AS total,\
        sum((status != '200 OK')::int)::float AS errcnt\
        FROM log\
        GROUP BY date) AS errors\
        WHERE errcnt/total > .01"
    cursor.execute(query)
    records = cursor.fetchall()
    db.close()
    print("\n" + "Days with more than 1% of requests lead to errors:")
    for record in records:
        print "\t" + str(record[0]) + " -- " + str(record[1]) + "%"


def main():
    poparticles()
    popauthors()
    requesterr()

if __name__ == '__main__':
    main()
