class GetDictParam:
    @classmethod
    def list_for_key_to_dict(cls, *args, my_dict) -> dict:
            result = {}
            if len(args) > 0:
                for key in args:
                    result.update({key: my_dict.get(key)})
            return result
