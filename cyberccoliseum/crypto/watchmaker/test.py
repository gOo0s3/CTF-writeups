emoji_dict = {
    '🕐': '13', '🕑': '14', '🕒': '15', '🕓': '16', '🕔': '17', '🕕': '18',
    '🕖': '19', '🕗': '20', '🕘': '21', '🕙': '22', '🕚': '23', '🕛': '24',
}

clock_string = "🕔 🕖 🕕 🕖 🕔 🕗 🕔 🕘 🕔 🕕 🕖 🕔 🕙 🕒 🕓 🕐 🕘 🕗 🕘 🕖 🕖 🕚 🕘 🕗 🕓 🕐 🕘 🕐 🕓 🕒 🕖 🕚 🕘 🕗 🕒 🕓 🕖 🕚 🕗 🕗 🕓 🕓 🕗 🕒 🕗 🕚 🕙 🕔".replace(" ", "")
times = [f"{emoji_dict[c]}" for c in clock_string]

for time in times:
    print(time, end=":")
