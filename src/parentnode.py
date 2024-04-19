from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        html = ""
        if not self.tag:
            raise ValueError()
        if not self.children:
            raise ValueError("Invalid HTML: no children")
        
        for child in self.children:
            html += child.to_html()
        
        return f'<{self.tag}>{html}</{self.tag}>'