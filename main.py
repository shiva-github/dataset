import pymysql.cursors
import time


def movie_data(filename):
	name, filetype = filename
	list1 = []
	listfinal = []
	i=0
	with open(name) as file1:
		for line in file1.readlines():
			for data in line.split("+++$+++"):
				list1.append(data.strip())
			listfinal.append(list1)
			list1 = []
			i +=1
			if i == 15: break

	return listfinal, filetype
##################################################
############### CREATE TABLE #####################
##################################################

def create_tbl(datalist,tableName):
	data = """CREATE TABLE IF NOT EXISTS
	 %s ( id INT AUTO_INCREMENT PRIMARY KEY, """ %(tableName)
	for x in datalist[:-1]:
		data += "%s %s %s, " %(x["name"], x["dtype"], x["other"])

	data += "%s %s %s) " %(datalist[-1]["name"], datalist[-1]["dtype"], datalist[-1]["other"])
	print(data)
	return True
##################################################
############### INSERT TABLE 1 ###################
##################################################

def table_insert1(datalist,tableName):
	dataInsert = []
	for x in datalist:
		data = """INSERT INTO %s VALUES (null, """ %(tableName)
		for y in x[:-1]:
			data += "'{}'," .format(y)
		data += "{} ) " .format(x[-1])
		dataInsert.append(data)
		data = []
	print(len(dataInsert))
	return True

##################################################
############### INSERT TABLE 2 ###################
##################################################

def table_insert2(datalist,tableName):
	dataInsert = []
	for x in datalist:
		data = """INSERT INTO %s VALUES (null, """ %(tableName)
		for y in x[:-1]:
			data += "'{}'," .format(y)
		data += "{} ) " .format(x[-1])
		dataInsert.append(data)
		data = []
	print(len(dataInsert))
	return True
##################################################
############### INSERT TABLE 3 ###################
##################################################

def table_insert3(datalist,tableName):
	dataInsert = []
	for x in datalist:
		data = """INSERT INTO %s VALUES (null, """ %(tableName)
		for y in x[:-1]:
			data += "'{}'," .format(y)
		data += "{} ) " .format(x[-1])
		dataInsert.append(data)
		data = []
	print(len(dataInsert))
	return True
##################################################
############### INSERT TABLE 4 ###################
##################################################

def table_insert4(datalist,tableName):
	dataInsert = []
	for x in datalist:
		data = """INSERT INTO %s VALUES (null, """ %(tableName)
		for y in x[:-1]:
			data += "'{}'," .format(y)
		data += "{} ) " .format(x[-1])
		dataInsert.append(data)
		data = []
	print(len(dataInsert))
	return True

##################################################
############### INSERT TABLE 5 ###################
##################################################

def table_insert5(datalist,tableName):
	dataInsert = []
	for x in datalist:
		data = """INSERT INTO %s VALUES (null, """ %(tableName)
		for y in x[:-1]:
			data += "'{}'," .format(y)
		data += "{} ) " .format(x[-1])
		dataInsert.append(data)
		data = []
	print(len(dataInsert))
	return True


##################################################
############### MAIN FUNCTION ####################
##################################################
def main():
	filename1 = "movie_characters_metadata.txt", "characters"
	filename2 = "movie_conversations.txt", "conversation"
	filename3 = "movie_lines.txt", "lines"
	filename4 = "movie_titles_metadata.txt", "titles"
	filename5 = "raw_script_urls.txt", "raw urls"
	datalist = [
		{"name": "charID", "dtype": "varchar(10)", "other": "NOT NULL" },
		{"name": "name", "dtype": "varchar(255)", "other": "NOT NULL" },
		{"name": "movieID", "dtype": "varchar(200)", "other": "NOT NULL" },
		{"name": "movieTitle", "dtype": "varchar(200)", "other": "NOT NULL" },
		{"name": "gender", "dtype": "varchar(10)", "other": "NULL" },
		{"name": "positionCredit", "dtype": "int", "other": "NULL" }
		]
	movie, filetype = movie_data(filename1)
	create_tbl(datalist, filetype)
	print("\n-------------------------------\n\n")
	# print(len(movie))
	# print(filetype)
	table_insert(movie, filetype)
	print("\n-------------------------------\n\n")
	# print(movie[12])
	print("\n-------------------------------\n\n")

	# movie = []
	# movie, filetype = movie_data(filename2)
	# print(filetype)
	# print(movie[0])
	# print("\n-------------------------------\n\n")
	# movie = []
	# movie, filetype = movie_data(filename3)
	# print(filetype)
	# print(movie[0])
	# print("\n-------------------------------\n\n")
	# movie = []
	# movie, filetype = movie_data(filename4)
	# print(filetype)
	# print(movie[0])
	# print("\n-------------------------------\n\n")
	# movie = []
	# movie, filetype = movie_data(filename5)
	# print(filetype)
	# print(movie[0])
	# print("\n-------------------------------\n\n")
if __name__ == '__main__':
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))