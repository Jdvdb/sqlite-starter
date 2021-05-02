# sqlite-starter
Python program to easily work with sqlite databases

## Getting Started
As long as you are running python version 3.7.4, this should work
Run the driver.py file as you would any other python file on your computer.
The program will then prompt you to either create a new database or work in an existing one.

The functionality can be found using the `help` keyword.
Additonal running instructions can be found bellow.

### Create Table
This can be accomplished using the command `create`
The first line of input will be the name of the table (e.g: `records`)
The next line of input will be the number of attributes in this table (e.g: `3`)

After this, you will be prompted to enter information for each attribute.
You can use the following keywords for the datatypes:
`integer` - INTEGER
`real` - REAL
`text` - TEXT
`blob` - BLOB

The status refers to if this is a key or a null value.
You can use the following keywords for the status:
`pk` - PRIMARY KEY
`nn` - NOT NULL
`fk __ __` - FOREIGN KEY

N.B. Using a foreign key requires additional input.
If you wanted it to reference `id` in `table`, use the command as follows:
`foreign_key_name integer fk table id`

N.B You can also use multiple attributes for a primary key as follows:
`id integer pk`
`name text pk`


Each attribute should be given in the following style: `att_name type status`

Here is an example table creation input for student records:
`students`
`3`
`id integer pk`
`name Text nn`
`num_friends integer`

### Get Columns