'''
This program is written in python3
It is required project( Log Analysis)
for udacity full stack web developer nanodegree
'''
import psycopg2  # to connect to the database(postgresql)
import sys  # to access system functions


# here is the function of connection to the database:
def connect_to_database(data_base="newsdata"):
    try:
        connection = psycopg2.connect(dbname=data_base)
        cursor = connection.cursor()
        return connection, cursor
    except psycopg2.Error as error:
        print("error in connecting the database")
        sys.exit(0)


''' here is the responsible function for committing 
the queries of the project '''

def fetch_query(query):
    connection, cursor = connect_to_database()
    cursor.execute(query)
    results = cursor.fechall()
    connection.close()
    return results


''' here is the responsible function for printing 
the 3 top popular articles'''

def print_top_3_popular_articles():
    first_query = '''select articles.title, count(log.id) as toal_reads from
     articles join log on log.path=('/article/'||articles.slug)
     group by articles.title
     order by total-reads desc
     limit 3'''
    query_results = fetch_query(first_query)
    print('1. What are the most popular three articles of all time?')
    print()
    for i in query_results:
        print("{} {} {} views".format('(i+1).', i[1], i[2]))
    print()


''' here is the responsible function for 
printing the most 4 popular authors '''

def print_top_4_popular_authors():
    second_query = '''select authors.name, count(log.id) as total
    from articles
     join authors on authors.id=articles.author
     join log on log.path=('/article/'||articles.slug)
     group by authors.name order by total desc limit 4;'''
    query_results = fetch_query(second_query)
    print('2. Who are the most popular article authors of all time?')
    print()
    for i in query_results:
        print("{} {} {} views".format('(i+1).', i[1], i[2]))
    print()


''' here is the responsible function for printing the days with error 
requests precentages more than 1% of requests '''

def print_days_of_error_requests():
    third_query = '''select
            to_char(errors_per_day.date,'Month DD, YYYY') as day_full_date,
            to_char(((errors_per_day.count::decimal/requests_per_day.count::decimal)*100)
                    ,'9.99')
                    || '%' as error_percentage
        from
            (select date(time),count(*) from log group by date(time)) as requests_per_day,
            (select date(time),count(*) from log where status != '200 OK' group by date(time)) as errors_per_day
        where
            requests_per_day.date = errors_per_day.date
            and ((errors_per_day.count::decimal
                    /requests_per_day.count::decimal)*100) > 1;'''
    query_results = fetch_query(third_query)
    print('3. On which days did more than 1% of requests lead to errors?')
    print()
    for i in query_results:
        print("{} {} {} views".format('(i+1).', i[1], i[2]))
    print()


if __name__ == '__main__':
    print_top_3_popular_articles()
    print_top_4_popular_authors()
    print_days_of_error_requests()
