if __name__ == '__main__':
    love_connections = [("Lysander", "Helena"), ('Hermia', 'Lysander'),
                        ('Demetrius', 'Hermia'), ('Helena', 'Demetrius'),
                        ('Titania', 'Oberon'), ('Oberon', 'Titania'),
                        ('Puck', None), ('Lysander', 'Puck')]

    adj_list = {}
    for source, target in love_connections:
        if source in adj_list:
            adj_list[source].append(target)
        else:
            adj_list[source] = [target]

    for neighbor in adj_list['Lysander']:
        print(neighbor)
