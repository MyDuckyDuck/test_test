# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: DeskQueue
class Template:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields  # dict: field_name -> type (str, int, datetime)

    @staticmethod
    def from_dict(name, spec):
        return Template(name, spec)

    def to_record(self, extra=None):
        record = {}
        for k, t in self.fields.items():
            if k == 'id': continue
            val = extra.get(k, '') if extra else ''
            record[k] = val
        if extra: record.update(extra)
        return DeskRecord(id='', fields=record)

    def create(self):
        rec = self.to_record()
        rec.id = str(uuid.uuid4())[:8]
        rec.created_at = datetime.now().isoformat()
        if 'status' not in rec.fields and 'status' not in rec:
            rec.status = 'pending'
        return rec

class TemplateManager:
    def __init__(self):
        self.templates = {}  # name -> Template

    def register(self, template):
        self.templates[template.name] = template

    @property
    def names(self):
        return list(self.templates.keys())

def main():
    tm = TemplateManager()
    tm.register(Template('task_default', {
        'title': str, 'priority': int, 'deadline': datetime
    }))
    print(tm.names)  # ['task_default']
