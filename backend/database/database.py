import asyncio
import json
import os
from typing import List, Dict, Optional, Any
from datetime import datetime
import aiofiles

class DatabaseManager:
    """Simple file-based database manager for development/demo purposes"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.complaints_file = os.path.join(data_dir, "complaints.json")
        self.service_requests_file = os.path.join(data_dir, "service_requests.json")
        self.feedback_file = os.path.join(data_dir, "feedback.json")
        
        # In-memory storage for better performance
        self.complaints = []
        self.service_requests = []
        self.feedback = []
    
    async def initialize(self):
        """Initialize database and load existing data"""
        # Create data directory if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Load existing data
        await self._load_complaints()
        await self._load_service_requests()
        await self._load_feedback()
    
    async def close(self):
        """Save all data and close connections"""
        await self._save_complaints()
        await self._save_service_requests()
        await self._save_feedback()
    
    # Complaint operations
    async def save_complaint(self, complaint_data: dict):
        """Save a new complaint"""
        # Convert datetime objects to ISO format strings
        complaint_data = self._serialize_datetime(complaint_data)
        self.complaints.append(complaint_data)
        await self._save_complaints()
    
    async def get_complaints(self, limit: int = 10, skip: int = 0) -> List[dict]:
        """Get complaints with pagination"""
        end_idx = skip + limit
        complaints = self.complaints[skip:end_idx]
        return [self._deserialize_datetime(c) for c in complaints]
    
    async def get_complaint_by_id(self, complaint_id: str) -> Optional[dict]:
        """Get complaint by ID"""
        for complaint in self.complaints:
            if complaint['id'] == complaint_id:
                return self._deserialize_datetime(complaint)
        return None
    
    async def update_complaint(self, complaint_id: str, complaint_data: dict):
        """Update an existing complaint"""
        complaint_data = self._serialize_datetime(complaint_data)
        for i, complaint in enumerate(self.complaints):
            if complaint['id'] == complaint_id:
                self.complaints[i] = complaint_data
                await self._save_complaints()
                return
        raise ValueError(f"Complaint {complaint_id} not found")
    
    async def get_complaints_by_status(self, status: str) -> List[dict]:
        """Get complaints filtered by status"""
        filtered = [c for c in self.complaints if c['status'] == status]
        return [self._deserialize_datetime(c) for c in filtered]
    
    async def get_complaints_by_category(self, category: str) -> List[dict]:
        """Get complaints filtered by category"""
        filtered = [c for c in self.complaints if c['category'] == category]
        return [self._deserialize_datetime(c) for c in filtered]
    
    async def get_complaints_by_unit(self, unit_number: str) -> List[dict]:
        """Get complaints for a specific unit"""
        filtered = [c for c in self.complaints if c['unit_number'] == unit_number]
        return [self._deserialize_datetime(c) for c in filtered]
    
    async def search_complaints(self, search_term: str) -> List[dict]:
        """Search complaints by title or description"""
        search_term = search_term.lower()
        filtered = [
            c for c in self.complaints 
            if search_term in c['title'].lower() or search_term in c['description'].lower()
        ]
        return [self._deserialize_datetime(c) for c in filtered]
    
    # Service Request operations
    async def save_service_request(self, request_data: dict):
        """Save a new service request"""
        request_data = self._serialize_datetime(request_data)
        self.service_requests.append(request_data)
        await self._save_service_requests()
    
    async def get_service_requests(self, limit: int = 10, skip: int = 0) -> List[dict]:
        """Get service requests with pagination"""
        end_idx = skip + limit
        requests = self.service_requests[skip:end_idx]
        return [self._deserialize_datetime(r) for r in requests]
    
    async def get_service_request_by_id(self, request_id: str) -> Optional[dict]:
        """Get service request by ID"""
        for request in self.service_requests:
            if request['id'] == request_id:
                return self._deserialize_datetime(request)
        return None
    
    async def update_service_request(self, request_id: str, request_data: dict):
        """Update an existing service request"""
        request_data = self._serialize_datetime(request_data)
        for i, request in enumerate(self.service_requests):
            if request['id'] == request_id:
                self.service_requests[i] = request_data
                await self._save_service_requests()
                return
        raise ValueError(f"Service request {request_id} not found")
    
    async def get_service_requests_by_status(self, status: str) -> List[dict]:
        """Get service requests filtered by status"""
        filtered = [r for r in self.service_requests if r['status'] == status]
        return [self._deserialize_datetime(r) for r in filtered]
    
    async def get_service_requests_by_type(self, service_type: str) -> List[dict]:
        """Get service requests filtered by type"""
        filtered = [r for r in self.service_requests if r['service_type'] == service_type]
        return [self._deserialize_datetime(r) for r in filtered]
    
    async def get_service_requests_by_unit(self, unit_number: str) -> List[dict]:
        """Get service requests for a specific unit"""
        filtered = [r for r in self.service_requests if r['unit_number'] == unit_number]
        return [self._deserialize_datetime(r) for r in filtered]
    
    async def get_service_requests_by_urgency(self, urgency_levels: List[str]) -> List[dict]:
        """Get service requests by urgency levels"""
        filtered = [r for r in self.service_requests if r['urgency'] in urgency_levels]
        return [self._deserialize_datetime(r) for r in filtered]
    
    async def search_service_requests(self, search_term: str) -> List[dict]:
        """Search service requests by title or description"""
        search_term = search_term.lower()
        filtered = [
            r for r in self.service_requests 
            if search_term in r['title'].lower() or search_term in r['description'].lower()
        ]