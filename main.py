
from data.repository import AdverseRepository
from visualization.adverse_visualizer import AdverseVisualizer

def main():
    repository = AdverseRepository()
    df = repository.get_adverse_data()

    visualizer = AdverseVisualizer()
    visualizer.adverse_event_and_gender(df)

if __name__ == "__main__":
    main()
