import matplotlib.pyplot as plt
import json
import database as db
from datetime import datetime, timedelta


def plot_weekdays(stats: list[dict]):
    weekdays = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
    avgs = db.usage_by_weekday(stats)
    print("A hét napjaira eső átlagos használati idők:")
    for index, day in enumerate(weekdays):
        print(f"{day}: {avgs[index]} perc")
    # TODO: Create pie chart 
    plt.pie(avgs, labels=weekdays, autopct="%1.1f%%")
    plt.savefig("weekdays.png")
    plt.close()


def plot_apps(stats: list[dict]):
    with open('category_colors.json', 'r') as f:
        category_colors = json.load(f)
    
    with open('apps.json', 'r') as f:
        app_categories = json.load(f)
    
    amounts = db.usage_by_app(stats)
    app_totals = sorted([(total, app) for app, total in amounts.items()], reverse=True)
    print("Az alkalmazások összesített használati idői:")
    for usage, app in app_totals:
        print(f"{app}: {usage} perc")
    
    apps = [app.upper() for _, app in app_totals]
    usages = [usage for usage, _ in app_totals]

    def get_app_category(app):
        for category, app_list in app_categories.items():
            if app.lower() in [a.lower() for a in app_list]:
                return category
    colors = [category_colors.get(get_app_category(app)) for app in apps]

    # TODO: Create barh chart
    apps = [app for _, app in app_totals]
    usages = [usage for usage, _ in app_totals]
    plt.barh(apps[::-1], usages[::-1])
    plt.xlabel("Usage (minutes)")
    plt.savefig("usage_by_app.png")
    plt.close()
    
    # TODO: Create colored barh chart
    plt.barh(apps[::-1], usages[::-1], color=colors[::-1])
    plt.xlabel("Usage (minutes)")
    plt.ylabel("App")
    plt.savefig("usage_by_apps_colored.png")
    plt.close()


def plot_categories(stats: list[dict]):
    category_totals = db.usage_by_category(stats)
    print("Kategóriánként összesített használati idők:")
    for category, total in category_totals.items():
        print(f"{category}: {total} perc")
    categories = list(category_totals.keys())
    totals = list(category_totals.values())

    with open('category_colors.json', 'r') as f:
        category_colors = json.load(f)
    with open('apps.json', 'r') as f:
        app_categories = json.load(f)

    def get_app_category(app):
        for category, app_list in app_categories.items():
            if app.lower() in [a.lower() for a in app_list]:
                return category
    
    category_totals = {cat: 0 for cat in app_categories.keys()}
    for entry in stats:
        app = entry.get('app_name')
        usage = entry.get('usage', 0)
        if app:
            category = get_app_category(app)
            if category not in category_totals:
                category_totals[category] = 0
            category_totals[category] += usage
    colors = [category_colors.get(cat) for cat in categories]
    # TODO: Create bar chart
    plt.bar(categories, totals, color=colors)
    plt.title("Total usage by category (minutes)")
    for i, total in enumerate(totals):
        plt.text(i, total + 1, str(total), ha='center', va='bottom')
    plt.savefig("usage_by_category.png")
    plt.close()
    
    # TODO: Create stacked barh chart
    start_date = datetime(year, month, 1)
    dates = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(31)]

    daily_usage = {cat: [0] * len(dates) for cat in categories}
    for entry in stats:
        app = entry.get('app_name')
        usage = entry.get('usage', 0)
        date = entry.get('date')
        if app and date:
            category = get_app_category(app)
            if category in daily_usage:
                date_index = dates.index(date) if date in dates else -1
                if date_index >= 0:
                    daily_usage[category][date_index] += usage

    bottom = [0] * len(dates)
    for cat in categories:
        plt.barh(dates, daily_usage[cat], left=bottom, color=category_colors.get(cat, "gray"), label=cat)
        bottom = [bottom[i] + daily_usage[cat][i] for i in range(len(dates))]
    plt.xlabel('Usage (minutes)')
    plt.ylabel('Day')
    plt.savefig('usage_by_category_stacked.png')
    plt.close()

if __name__ == "__main__":
    year = int(input("year = "))
    month = int(input("month = "))
    stats = db.read_usages(year, month)
    plot_weekdays(stats)
    plot_apps(stats)
    plot_categories(stats)

