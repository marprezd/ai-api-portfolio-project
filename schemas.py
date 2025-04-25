"""Pydantic schemas for the api."""
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import date

class Performance(BaseModel):
    """Performance model"""
    model_config = ConfigDict(from_attributes=True)
    performance_id: int
    week_number: str
    fantasy_points: float
    last_changed_date: date

class PlayerBase(BaseModel):
    """Base model for Player"""
    model_config = ConfigDict(from_attributes=True)
    player_id: int
    gsis_id: str
    first_name: str
    last_name: str
    position: str
    last_changed_date: date
        
class Player(PlayerBase):
    """Player model"""
    model_config = ConfigDict(from_attributes=True)
    performances: List[Performance] = []

class TeamBase(BaseModel):
    """Base model for team"""
    model_config = ConfigDict(from_attributes=True)
    league_id: int
    team_id: int
    team_name: str
    last_changed_date: date

class Team(TeamBase):
    """Team model"""
    model_config = ConfigDict(from_attributes=True)
    players: List[PlayerBase] = []

class League(BaseModel):
    """League model"""
    model_config = ConfigDict(from_attributes=True)
    league_id: int
    league_name: str
    scoring_type: str
    last_changed_date: date
    teams: List[TeamBase] = []

class Counts(BaseModel):
    """Counts model"""
    league_count: int
    team_count: int
    player_count: int