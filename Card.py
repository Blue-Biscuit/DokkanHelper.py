################################################################################
### Defines a couple of types and methods for dealing with Dokkan card data. ###
################################################################################

def stats(hp: int, attack: int, defence: int):
    """Builds a 'stats' instance."""
    return {
        "HP" : hp,
        "ATK" : attack,
        "DEF" : defence
    }

class PassiveSkill:
    """Defines a passive skill for a Dokkan Battle card."""

    def __init__(self):
        self._data = [] # The passive skill's body data.
    
    def appendClause(self, text: str, statsBoost, percentage: bool = True):
        """Appends a unique clause to the passive skill."""
        self._data.append({"text" : text, "boost" : statsBoost, "percentage" : percentage})
    
    def __str__(self):
        result = ''

        for i in range(0, len(self._data) - 1):
            text = self._data[i]["text"]
            result += f'{text}; '
        
        text = self._data[len(self._data) - 1]["text"]
        result += text

        return result

if __name__ == "__main__":
    skill = PassiveSkill()

    skill.appendClause("First clause", stats(100, 100, 100))
    skill.appendClause("Second clause", stats(100, 100, 100))

    print(skill)