def list_sessions_query(limit: int = 100, offset: int = 0):
    return f"""
        ?[
            agent_id,
            user_id,
            id,
            situation,
            summary,
            updated_at,
            created_at,
        ] :=
            *sessions{{
                session_id: id,
                situation,
                summary,
                created_at,
                updated_at: validity,
                @ "NOW"
            }},
            *session_lookup{{
                agent_id,
                user_id,
                session_id,
            }}, updated_at = to_int(validity)

        :limit {limit}
        :offset {offset}
        :sort -created_at
    """
