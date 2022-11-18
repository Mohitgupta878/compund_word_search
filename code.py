import os
loc = r"H:\code_impledge"
os.chdir(loc)

global A
def read_text_file(file_path):
    with open(file_path, 'r') as new_file:
        A = new_file.read().split()
    S = set(A)
    ans = []
    for wrd in A:
        if not wrd: continue
        st = [0]
        dict1 = {0}
        total_len = len(wrd)
        while st:
            data = st.pop()
            if data == total_len:
                ans.append(wrd)
                break
            for j in range(total_len - data + 1):
                if (wrd[data:data+j] in S and data + j not in dict1 and (data > 0 or data + j != total_len)):
                    st.append(data + j)
                    dict1.add(data + j)
                
    res = sorted(ans,key = lambda x: (-len(x),x))
    print("Longest Compound Word :" , res[0])
    print("Second Longest Compound Word :" ,res[1])
for file in os.listdir():
	if file.endswith(".txt"):
		file_path = f"{loc}\{file}"
		read_text_file(file_path)
