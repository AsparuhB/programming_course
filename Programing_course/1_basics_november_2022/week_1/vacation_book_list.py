#Summer literature. We need to find how many hours per day George he will need to read to complete the task

num_pages = int(input())
#Need how many pages per day he needs to read from the book
pages_per_hour = int(input())
#We need to input how many pages per hour can he read
days = int(input())
# How many days he needs to read 1 book.

#We need to find the number of hours reading per day he needs to complete a book.

total_read_time = num_pages / pages_per_hour
#Need to calculate the total read time by dividing the number of pages in the book by the pages he reads per hour.
book_time = total_read_time // days
#to find the total days he needs to read the whole book, we need to divide the total reading time by the days he has
print(book_time)