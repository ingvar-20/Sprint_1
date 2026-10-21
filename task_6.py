types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 

def del_duplicates(all_tickets):
    seen_tickets = []
    result = {}
    for r in range(1, 6):
        unique_tickets = []
        for ticket in all_tickets[r]:
            if ticket not in seen_tickets:
                unique_tickets.append(ticket)
                seen_tickets.append(ticket)
        result[r] = unique_tickets
    return result

def link_types(bug_types, all_tickets):
    cleaned = del_duplicates(all_tickets)
    result = {}
    for r in range(1, 6):
        result[bug_types[r]] = cleaned[r]
    return result

tickets_by_type = link_types(types, tickets)
print(tickets_by_type)