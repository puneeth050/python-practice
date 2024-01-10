from dis import dis
  
page = 45
n = 80

def abbreviated_pages(n, page):
    pageList = []
    """
    Return a string containing the list of numbers from 1 to `n`, with
    `page` indicated, and abbreviated with ellipses if too long.

    >>> abbreviated_pages(5, 3)
    '1 2 [3] 4 5'
    >>> abbreviated_pages(10, 10)
    '1 2 3 4 5 6 7 8 9 [10]'
    >>> abbreviated_pages(20, 1)
    '[1] 2 3 ... 18 19 20'
    >>> abbreviated_pages(80, 30)
    '1 2 3 ... 28 29 [30] 31 32 ... 78 79 80'
    """
    assert(0 < n)
    assert(0 < page <= n)

    # Build set of pages to display
    if n <= 10:
        pages = set(range(1, n + 1))
    else:
        pages = (set(range(1, 4))
                 | set(range(max(1, page - 2), min(page + 3, n + 1)))
                 | set(range(n - 2, n + 1)))
    print('pages:', pages)
   
# Display pages in order with ellipses
    def display():
        last_page = 0
        
        for p in sorted(pages):
            if p != last_page + 1:
                yield '-'
                pageList.append('-')
            yield ('{0}' if p == page else '{0}').format(p)
            last_page = p
            print(last_page)
            pageList.append(last_page)
    return ' '.join(display())

import pandas as pd

def main():
    # creating the DataFrame
    marks_data = pd.DataFrame({'ID': {0: 23, 1: 43, 2: 12,
                                    3: 13, 4: 67, 5: 89,
                                    6: 90, 7: 56, 8: 34},
                            'Name': {0: 'Ram', 1: 'Deep',
                                    2: 'Yash', 3: 'Aman',
                                    4: 'Arjun', 5: 'Aditya',
                                    6: 'Divya', 7: 'Chalsea',
                                    8: 'Akash' },
                            'Marks': {0: 89, 1: 97, 2: 45, 3: 78,
                                        4: 56, 5: 76, 6: 100, 7: 87,
                                        8: 81},
                            'Grade': {0: 'B', 1: 'A', 2: 'F', 3: 'C',
                                        4: 'E', 5: 'C', 6: 'A', 7: 'B',
                                        8: 'B'}})
    
    # determining the name of the file
    file_name = 'MarksData.xlsx'
    
    # saving the excel
    marks_data.to_excel(file_name)
    print('DataFrame is written to Excel File successfully.')

if __name__ == '__main__':
    # a = abbreviated_pages(n, page);
    # print(a)
    main()
    