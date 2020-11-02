import csv

class EP4:

    dataset = {}

    def createDataset(self):
        with open('EP4/imdb-reviews-pt-br.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            index = 0
            skip = True
            justPTBR = []
            for item in reader:
                if skip:
                    skip = False
                    continue
                newItem = item
                newItem.pop(1)
                newItem.pop(0)
                justPTBR.append(newItem)
                if index == 4:
                    break
                else:
                    index += 1

            index = 0
            for item in justPTBR:
                self.dataset[index] = item
                index += 1
            print(self.dataset)


            


            # index = 0
            # for item in reader:
            #     # for 
            #     print()
            #     print(item)
            #     print()
            #     if index == 2:
            #         break
            #     else:
            #         index += 1
            
        # print(self.dataset)

ep4 = EP4()
ep4.createDataset()

                