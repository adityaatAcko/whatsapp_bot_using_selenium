import psycopg2
import psycopg2.extras

def show_policy_by_no(number):
    try:
        conn = psycopg2.connect("dbname=acko user=aditya password=postgres")
        #conn = psycopg2.connect(host="13.233.55.204", database="acko", user="ubuntu", port="5432")

        cur = conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
        cur.execute("SELECT id,plan_id,data->'premium'->>'amount' as premium_amount,created_on FROM ackore_policy where data->>'phone' = %(some_no)s  ORDER BY created_on",{'some_no':number})
        #print("The number of policies: ", cur.rowcount)
        rows=cur.fetchall()
        print(rows)
        #for row in rows:
         #   print(row.id)
          #  print(row.plan_id)
        return rows



    except Exception as e:
        print(e)


if __name__=="__main__":
    show_policy_by_no("7895928293")