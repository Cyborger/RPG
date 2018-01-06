class InteractionHandler:
    def __init__(self, playing_state):
        self.state = playing_state

    def check_for_passage_interaction(self):
        for passage in self.state.current_location.passages:
            if self.state.player.rect.colliderect(passage.rect):
                new_passage = self.state.game.get_passage(passage.passage_to)
                self.state.change_location(new_passage.location)
                new_passage.update_player_position(self.state.player)

    def check_for_npc_interaction(self):
        for npc in self.state.current_location.npcs:
            if self.state.player.rect.colliderect(npc.rect):
                self.state.game.dialogue_state.set_messages(npc.messages)
                self.state.game.dialogue_state.update_name_label(npc.name)
                self.state.game.change_state(self.state.game.dialogue_state)
                break

    def check_for_chest_interaction(self):
        for chest in self.state.current_location.chests:
            if self.state.player.rect.colliderect(chest.rect):
                if not chest.opened:
                    chest.open()
                    break
