class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag:str = tag
        self.value:str = value
        self.children:list = children
        self.props:dict = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self)->str:
        if self.props is None:
            return ""
        
        output = ""
        for key in self.props.keys():
            output += f' {key}="{self.props[key]}"'
        
        return output

    def __repr__(self) -> str:
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
