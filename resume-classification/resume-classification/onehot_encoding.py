import csv 

def extract_skills():
    with open("final_datasets/complete_dataset.csv","r") as f:
        skills_list = []
        csvfile = csv.reader(f)
        for data in csvfile: 
            for value in data[3:]: 
                if value not in skills_list:
                    skills_list.append(value)
        return sorted(skills_list)

def create_dataset(): 
    skills_list = extract_skills()
    dataset = []
    with open("final_datasets/complete_dataset.csv","r") as f:
        csvfile = csv.reader(f)
        for data in csvfile:
            skills_bin = []
            for skill in skills_list:
                if skill in data[3:]:
                    skills_bin.append(1)
                else:
                    skills_bin.append(0)
            dataset.append(data[:3] +  skills_bin)
    return dataset
           
def create_csv_file():
    skills_list = extract_skills()

    with open("final_datasets/encoded_dataset.csv","w") as f:
        csvfile = csv.writer(f)
        row = ["Id","Name","Streams"] + skills_list
        csvfile.writerow(row)
        csvfile.writerows(create_dataset())
        


if __name__ == "__main__":
    create_csv_file()
 



