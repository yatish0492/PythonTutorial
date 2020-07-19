'''

Django supports 'for' loop in html file like angular js
-------------------------------------------------------
    Consider, 'destinations' is list of objects with each object containing 'name' and 'country'. Then the for loop
    in html file looks as follows,

            {% for dest in destinations %}

                {{dest.name}}
                {{dest.country}}

            {% endfor %}



Django supports 'if' condition in html file like angular js
-----------------------------------------------------------
    Consider, we have a variable 'abc' then the 'if' condition  in html file looks as follows,

            {% if abc==True %}      OR     {% if abc %} --> Implicitly it consider 'abc == True'

            <Some html code>

            {% endif %}


'''