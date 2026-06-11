class Solution:
    def applySubstitutions(self, replacements, text):
        raw = dict(replacements)     # key -> raw value (may hold placeholders)
        memo = {}                    # key -> fully resolved value

        def parse(s):
            # Splits string into literal parts and %KEY% parts
            # Example: "abc%B%" -> ["abc", "%B%"]
            parts = re.split(r'(%[A-Z]%)', s)
            res = []
            for p in parts:
                if not p: continue
                if p.startswith('%') and p.endswith('%'):
                    res.append(("key", p[1:-1]))
                else:
                    res.append(("lit", p))
            return res

        def resolve(key):
            if key in memo:
                return memo[key]
            out = []
            for kind, chunk in parse(raw[key]):
                if kind == "lit":
                    out.append(chunk)
                else:
                    out.append(resolve(chunk))
            memo[key] = "".join(out)
            return memo[key]

        # the top-level text is parsed the same way
        out = []
        for kind, chunk in parse(text):
            out.append(chunk if kind == "lit" else resolve(chunk))
        return "".join(out)