from html import escape

STORIES = {
    'OneGauge': {
        'problem': 'Custom vehicle configurations need specialized firmware. The product direction is to make more of that configuration accessible through a customer-facing application.',
        'role': 'I lead software technology decisions, develop embedded firmware, and help shape the application and the move toward a more configurable platform.',
        'tradeoff': 'Custom firmware can address a specific vehicle closely. A configurable platform needs to support that variety while making setup easier for customers. That balance is central to the direction of this work.',
        'status': 'Ongoing professional work: firmware development and application design/development. The diagram shows the intended relationship between the product components, not a released feature list.',
        'caption': 'Product direction · high-level view',
        'nodes': [('Vehicle data', 'Vehicle-specific inputs'), ('Gauge firmware', 'Embedded processing'), ('Customer application', 'Configuration & visualization')],
        'flow': 'Vehicle data informs the gauge firmware. The application is being developed to support configuration and vehicle-data visualization.'
    },
    'Luther': {
        'problem': 'A doctoral researcher needs to work across medieval-history journals and identify material relevant to potential research questions.',
        'role': 'I built a research tool around that workflow, bringing journal content, article and issue summaries, and potential research gaps together.',
        'tradeoff': 'Summaries can make a body of material easier to explore, but they do not replace reading the sources. Suggested research gaps are starting points for investigation, not established findings.',
        'status': 'Built personal project. This diagram describes the research workflow at a high level; it does not imply a specific underlying technology stack.',
        'caption': 'Research workflow · high-level view',
        'nodes': [('Journal content', 'Medieval-history sources'), ('AI-assisted synthesis', 'Article & issue summaries'), ('Research exploration', 'Potential questions & gaps')],
        'flow': 'Journal content supports summaries, which help surface potential research questions for a researcher to evaluate.'
    },
    'Vera': {
        'problem': 'Personal workflows span separate services and repeated tasks. I want to explore how local infrastructure can connect those pieces with meaningful human oversight.',
        'role': 'I am designing a local-first personal automation platform around service integrations and connected workflows.',
        'tradeoff': 'Automation can reduce repetitive effort, but consequential actions need deliberate review. Human approval is a design requirement before external actions with meaningful consequences.',
        'status': 'In design/development. This is a conceptual workflow, not a claim that every component is implemented or connected.',
        'caption': 'Concept architecture · in development',
        'nodes': [('Connected services', 'Information & requests'), ('Local workflows', 'Coordinate automation'), ('Human approval', 'Review consequential actions'), ('External action', 'Proceed after approval')],
        'flow': 'Connected services feed local workflows. Consequential external actions pass through human approval before proceeding.'
    }
}

def story(name):
    data = STORIES[name]
    blocks = ''.join(f'<div><h4>{label}</h4><p>{escape(data[key])}</p></div>' for key, label in [('problem', 'The problem'), ('role', 'My role'), ('tradeoff', 'The design tradeoff'), ('status', 'Where it stands')])
    nodes = ''.join(f'<li><strong>{escape(title)}</strong><span>{escape(detail)}</span></li>' for title, detail in data['nodes'])
    return f'''<details class="project-story"><summary><span class="story-closed">Explore the project</span><span class="story-open">Close project story</span><span class="sr-only">: {name}</span><span class="story-toggle" aria-hidden="true">+</span></summary><div class="story-content"><div class="story-grid">{blocks}</div><figure class="story-diagram"><figcaption>{escape(data['caption'])}</figcaption><ol class="story-flow">{nodes}</ol><p>{escape(data['flow'])}</p></figure></div></details>'''
