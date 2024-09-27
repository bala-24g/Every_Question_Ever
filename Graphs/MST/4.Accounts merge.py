from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def findroot(person):
            if parent[person] != person:
                parent[person] = findroot(parent[person])
            return parent[person]
        
        parent = list(range(len(accounts)))
        mails_account_mapping = {}

        # Union step: connect all emails within the same account
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in mails_account_mapping:
                    # Union the current account with the account that already contains this email
                    parent[findroot(i)] = findroot(mails_account_mapping[email])
                else:
                    mails_account_mapping[email] = i

        # Collect emails under the same parent account
        emails_under_parent = defaultdict(set)

        for i, account in enumerate(accounts):
            root = findroot(i)
            for email in account[1:]:
                emails_under_parent[root].add(email)

        # Prepare the result
        merged = []
        for parent_index, emails in emails_under_parent.items():
            sorted_emails = sorted(emails)
            account_name = [accounts[parent_index][0]]
            merged_account = account_name + sorted_emails
            merged.append(merged_account)

        return merged
#You first create the parents to each account by keeping a track of visited email ids and the account associated with them.
# Maintain a dictionary to serve as your ID:MAILS mapping.
# Then you traverse through each id, and add the accounts to them by going to its parent and adding to its set.
#Finally, return the answer by making the dictionary into an array form.