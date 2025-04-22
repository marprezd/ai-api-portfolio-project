"""SQLAlchemy models"""
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from database import Base

class Player(Base):
    """Player model"""
    __tablename__ = 'player'

    player_id = Column(Integer, primary_key=True, index=True)
    gsis_id = Column(String, nullable=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    last_changed_date = Column(Date, nullable=False)

    # Foreign key relationship to Team table
    # One-to-many relationship between Player and Performance tables
    performances = relationship("Performance", back_populates="player")

    # Many-to-many relationship between Player and Team tables
    teams = relationship("Team", secondary="team_player", back_populates="players")

class Performance(Base):
    """Performance model"""
    __tablename__ = 'performance'

    performance_id = Column(Integer, primary_key=True, index=True)
    week_number = Column(String, nullable=False)
    fantasy_points = Column(Float, nullable=False)
    last_changed_date = Column(Date, nullable=False)

    # Foreign key to Player table
    # This is a many-to-one relationship between Performance and Player tables
    player_id = Column(Integer, ForeignKey('player.player_id'))
    
    # Foreign key relationship to Player table
    # One-to-many relationship between Player and Performance tables
    player = relationship("Player", back_populates="performances")

class League(Base):
    """League model"""
    __tablename__ = 'league'

    league_id = Column(Integer, primary_key=True, index=True)
    league_name = Column(String, nullable=False)
    scoring_type = Column(String, nullable=False)
    last_changed_date = Column(Date, nullable=False)

    # One-to-many relationship between League and Team tables
    teams = relationship("Team", back_populates="league")

class Team(Base):
    """Team model"""
    __tablename__ = 'team'

    team_id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String, nullable=False)
    league_id = Column(Integer, ForeignKey('league.league_id'))
    last_changed_date = Column(Date, nullable=False)

    # Foreign key relationship to League table
    # One-to-many relationship between League and Team tables
    league = relationship("League", back_populates="teams")

    # Many-to-many relationship between Team and Player tables
    players = relationship("Player", secondary="team_player", back_populates="teams")

class TeamPlayer(Base):
    """Association table for many-to-many relationship between Team and Player"""
    __tablename__ = 'team_player'

    team_id = Column(Integer, ForeignKey('team.team_id'), primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey('player.player_id'), primary_key=True, index=True)
    last_changed_date = Column(Date, nullable=False)