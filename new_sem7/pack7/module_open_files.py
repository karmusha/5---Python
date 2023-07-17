from io import TextIOWrapper

def end_of_gens(gens):
   res_dict = {}

   for i in range(0, len(gens)):
       res_dict[gens[i]] = False
    
   return res_dict

def zip_longest(*file_handlers):
    def generator(handle: TextIOWrapper):
        while True:
            for item in handle:
                yield item

            yield None
            handle.seek(0, 0)

    gens = [generator(handle) for handle in file_handlers]
    ends: dict = end_of_gens(gens)

    while not all(ends.values()):
        res: list = []
        for gen in gens:
            e = next(gen)
            if e is None:
                ends[gen] = True

                if all(ends.values()):
                    return

                e = next(gen)

            res.append(e)
        
        yield res

def file_processing(file_with_numbers, file_with_names, res_file):

    with (open(file_with_numbers, mode='r', encoding='utf-8') as nums,
        open(file_with_names, mode='r', encoding='utf-8') as names,
        open(res_file, mode='w', encoding='utf-8') as res):

        for items in zip_longest(nums, names):
            name: str = items[1]
            a, b = tuple(map(float,items[0].split(':')))
            prod = a * b

            if prod < 0:
                name = name.lower()
                prod = str(abs(prod))
            elif prod >= 0:
                name = name.upper()
                prod = str(round(prod))
            res.write(' / '.join([prod, name]))
    
if __name__ == '__main__':
    file_processing('new_sem7.txt', 'new_sem77.txt', 'new_sem7_mult.py')

