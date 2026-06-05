
class Solution:
    # KEY INSIGHTS 1: 
    # Even if two accounts have the same name, they may belong to different people. 
    # So we need to use a seperate dictionary to check the email with the account
    # assign email -> index 
    # It is something gonna look like this. 
    # email_to_idx = {
    #     "neet@gmail.com":     0,
    #     "neet_dsa@gmail.com": 0,
    #     "bob@gmail.com":      2,   # ← owned by index 2
    #     "alice@gmail.com":    1,
    #     "neetcode@gmail.com": 3,
    # }


    # KEY INSIGHTS 2: 
    # The rest of this problem is just set() checkin already in the set technique
    # that use for union find

    def __init__(self): 
        self.par = {}  # self.par = {0: 0, 1: 1, 2: 2, 3: 3}
        self.rank = {} # self.rank = {0: 0, 1: 0, 2: 0, 3: 0}

        self.email_to_idx = {} # {email: index parent node}
    
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 1. each account index starts as it own group
        for i in range(len(accounts)): 
            self.par[i] = i
            self.rank[i] = 0

        # 2. scan emails, union account that share one
        email_to_idx = {} 
        # KEY: We need to use enumerate here because we want to take the index as the root node
        #      not the name
        for i, account in enumerate(accounts):  # i = 0, account = ["neet", ...]
            for email in account[1:] :          # skip the name, take the email only
                if email in email_to_idx:       # if email already existed from the past account
                    self.union(i, email_to_idx[email]) # then unite the current indices and the email's indice 
                else: 
                    email_to_idx[email] = i     # else: add new email's indice to the dictionary
            

        # 3. gather emails by group root
        # KEY CODE TECHNIQUE: defaultdict(set) is a dictionary 
        #    that auto-creates an empty set the first time you touch a missing key
        group = defaultdict(set) 
        for email, i in email_to_idx.items(): # .items() hands you each pair as a tuple (key, value) ("neet@gmail.com", 0), ("neet_dsa@gmail.com", 0), ("alice@gmail.com", 1),
            # iteration 1: email = "neet@gmail.com",     i = 0
            # iteration 2: email = "neet_dsa@gmail.com", i = 0
            # iteration 3: email = "alice@gmail.com",     i = 1
            root = self.find(i) # translate "owner index" → "group ID" to find which person this belongs to
            group[root].add(email) 
        

        res = [] 
        for root, emails in group.items(): 
            name = accounts[root][0] 
            res.append([name] + sorted(emails))
        
        return res 

        
        
        



            

        