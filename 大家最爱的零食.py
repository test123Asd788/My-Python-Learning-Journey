def snack_vote():
    # 统计零食和对应的票数
    snacks = {
        '爆米花': int(input("爆米花票数：")),
        '薯片': int(input("薯片票数：")),
        '巧克力': int(input("巧克力票数：")),
        '紫菜': int(input("紫菜票数："))
    }
    
    # 统计票数
    total = sum(snacks.values())
    max_votes = max(snacks.values())
    favorite = [s for s, v in snacks.items() if v == max_votes]
    
    # 输出统计结果
    print(f"\n总票数：{total}")
    print(f"最高票：{max_votes}")
    print(f"最受欢迎：{'、'.join(favorite)}")
    
    # 输出排名
    print("\n排名：")
    for i, (s, v) in enumerate(sorted(snacks.items(), key=lambda x: x[1], reverse=True), 1):
        
        percentage = (v / total) * 100
        # 输出排名、零食名、票数和百分比
        print(f"{i}. {s} {v}票 ({percentage:.1f}%)")

